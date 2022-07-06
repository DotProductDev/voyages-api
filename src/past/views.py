from django.shortcuts import render
from django.db.models import Q,Prefetch
from django.http import HttpResponse, JsonResponse
from rest_framework.schemas.openapi import AutoSchema
from rest_framework import generics
from rest_framework.metadata import SimpleMetadata
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
import urllib
import json
import requests
import time
from .models import *
from .serializers import *
import pprint
from tools.nest import *
from tools.reqs import *
import collections

enslaved_options=options_handler('past/enslaved_options.json',hierarchical=False)
enslaver_options=options_handler('past/enslaver_options.json',hierarchical=False)

class SingleEnslaved(generics.GenericAPIView):
	def get(self,request,enslaved_id):
		enslaved_record=Enslaved.objects.get(pk=enslaved_id)
		serialized=EnslavedSerializer(enslaved_record,many=False).data
		return JsonResponse(serialized,safe=False)

class SingleEnslavedVar(TemplateView):
	template_name='singlevar.html'
	def get(self,request,enslaved_id,varname):
		enslaved_record=Enslaved.objects.get(pk=enslaved_id)
		serialized=EnslavedSerializer(enslaved_record,many=False).data
		keychain=varname.split('__')
		bottomval=bottomout(serialized,list(keychain))
		var_options=enslaved_options[varname]
		data={
			'enslaved_id':enslaved_id,
			'variable_api_name':varname,
			'variable_label':var_options['flatlabel'],
			'variable_type':var_options['type'],
			'variable_value':bottomval
		}
		context = super(SingleEnslavedVar, self).get_context_data()
		context['data']=data
		return context

#LONG-FORM TABULAR ENDPOINT. PAGINATION IS A NECESSITY HERE!
##HAVE NOT YET BUILT IN ORDER-BY FUNCTIONALITY
class EnslavedList(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	serializer_class=EnslavedSerializer
	def options(self,request):
		j=options_handler('past/enslaved_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		st=time.time()
		times=[]
		labels=[]
		print("+++++++\nusername:",request.auth.user)
		print("FETCHING...")
		queryset=Enslaved.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,request,enslaved_options,auto_prefetch=True)
		if len(error_messages)==0:
			headers={"next_uri":next_uri,"prev_uri":prev_uri,"total_results_count":results_count}
			read_serializer=EnslavedSerializer(queryset,many=True)
			serialized=read_serializer.data
			
			outputs=[]
		
			hierarchical=request.POST.get('hierarchical')
			if str(hierarchical).lower() in ['false','0','f','n']:
				hierarchical=False
			else:
				hierarchical=True
		
			if hierarchical==False:
				if selected_fields==[]:
					selected_fields=[i for i in enslaved_options]
			
				for s in serialized:
					d={}
					for selected_field in selected_fields:
						keychain=selected_field.split('__')
						bottomval=bottomout(s,list(keychain))
						d[selected_field]=bottomval
					outputs.append(d)
			else:
				outputs=serialized
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(outputs,safe=False,headers=headers)
		else:
			return JsonResponse({'status':'false','message':' | '.join(error_messages)}, status=500)




#This will only accept one field at a time
#Should only be a text field
#And it will only return max 10 results
#It will therefore serve as an autocomplete endpoint
#I should make all text queries into 'or' queries
class EnslavedTextFieldAutoComplete(generics.GenericAPIView):
	serializer_class=EnslavedSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		print("+++++++\nusername:",request.auth.user)
		try:
			st=time.time()
			params=dict(request.POST)
			k=next(iter(params))
			v=params[k][0]
			retrieve_all=True
			queryset=Enslaved.objects.all()		
			kwargs={'{0}__{1}'.format(k, 'icontains'):v}
			queryset=queryset.filter(**kwargs)
			queryset=queryset.prefetch_related(k)
			queryset=queryset.order_by(k)
			results_count=queryset.count()
			fetchcount=20
			vals=[]
			for v in queryset.values_list(k).iterator():
				if v not in vals:
					vals.append(v)
				if len(vals)>=fetchcount:
					break
			def flattenthis(l):
				fl=[]
				for i in l:
					if type(i)==tuple:
						for e in i:
							fl.append(e)
					else:
						fl.append(i)
				return fl
			val_list=flattenthis(l=vals)
			output_dict={
				k:val_list,
				"results_count":results_count
			}
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(output_dict,safe=False)
		except:
			print("failed\n+++++++")
			return JsonResponse({'status':'false','message':'bad autocomplete request'}, status=400)

class EnslaverTextFieldAutoComplete(generics.GenericAPIView):
	serializer_class=EnslaverSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		print("+++++++\nusername:",request.auth.user)
		try:
			st=time.time()
			params=dict(request.POST)
			k=next(iter(params))
			v=params[k][0]
			retrieve_all=True
			queryset=EnslaverIdentity.objects.all()		
			kwargs={'{0}__{1}'.format(k, 'icontains'):v}
			queryset=queryset.filter(**kwargs)
			queryset=queryset.prefetch_related(k)
			queryset=queryset.order_by(k)
			results_count=queryset.count()
			fetchcount=20
			vals=[]
			for v in queryset.values_list(k).iterator():
				if v not in vals:
					vals.append(v)
				if len(vals)>=fetchcount:
					break
			def flattenthis(l):
				fl=[]
				for i in l:
					if type(i)==tuple:
						for e in i:
							fl.append(e)
					else:
						fl.append(i)
				return fl
			val_list=flattenthis(l=vals)
			output_dict={
				k:val_list,
				"results_count":results_count
			}
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(output_dict,safe=False)
		except:
			print("failed\n+++++++")
			return JsonResponse({'status':'false','message':'bad autocomplete request'}, status=400)



#LONG-FORM TABULAR ENDPOINT. PAGINATION IS A NECESSITY HERE!
##HAVE NOT YET BUILT IN ORDER-BY FUNCTIONALITY
class EnslaverList(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	serializer_class=EnslaverSerializer
	def options(self,request):
		j=options_handler('past/enslaver_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		print("+++++++\nusername:",request.auth.user)
		print("FETCHING...")
		st=time.time()
		queryset=EnslaverIdentity.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,request,enslaver_options,auto_prefetch=True)
		if len(error_messages)==0:
			headers={"next_uri":next_uri,"prev_uri":prev_uri,"total_results_count":results_count}
			read_serializer=EnslaverSerializer(queryset,many=True)
			serialized=read_serializer.data
			
			outputs=[]
		
			hierarchical=request.POST.get('hierarchical')
			if str(hierarchical).lower() in ['false','0','f','n']:
				hierarchical=False
			else:
				hierarchical=True
		
			if hierarchical==False:
				if selected_fields==[]:
					selected_fields=[i for i in enslaver_options]
			
				for s in serialized:
					d={}
					for selected_field in selected_fields:
						keychain=selected_field.split('__')
						bottomval=bottomout(s,list(keychain))
						d[selected_field]=bottomval
					outputs.append(d)
			else:
				outputs=serialized
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(outputs,safe=False,headers=headers)
		else:
			return JsonResponse({'status':'false','message':' | '.join(error_messages)}, status=500)


# Basic statistics
## takes a numeric variable
## returns its sum, average, max, min, and stdv
class EnslavedAggregations(generics.GenericAPIView):
	serializer_class=EnslavedSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		st=time.time()
		print("+++++++\nusername:",request.auth.user)
		params=dict(request.POST)
		aggregations=params.get('aggregate_fields')
		print("aggregations:",aggregations)
		queryset=Enslaved.objects.all()
		
		aggregation,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,request,enslaved_options,retrieve_all=True)
		output_dict={}
		if len(error_messages)==0 and type(aggregation)==list:
			for a in aggregation:
				for k in a:
					v=a[k]
					fn=k.split('__')[-1]
					varname=k[:-len(fn)-2]
					if varname in output_dict:
						output_dict[varname][fn]=a[k]
					else:
						output_dict[varname]={fn:a[k]}
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(output_dict,safe=False)
		else:
			print("failed\n+++++++")
			return JsonResponse({'status':'false','message':' | '.join(error_messages)}, status=400)

# Basic statistics
## takes a numeric variable
## returns its sum, average, max, min, and stdv
class EnslaverAggregations(generics.GenericAPIView):
	serializer_class=EnslaverSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		st=time.time()
		print("+++++++\nusername:",request.auth.user)
		params=dict(request.POST)
		aggregations=params.get('aggregate_fields')
		print("aggregations:",aggregations)
		queryset=EnslaverIdentity.objects.all()
		
		aggregation,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,request,enslaver_options,retrieve_all=True)
		output_dict={}
		if len(error_messages)==0 and type(aggregation)==list:
			for a in aggregation:
				for k in a:
					v=a[k]
					fn=k.split('__')[-1]
					varname=k[:-len(fn)-2]
					if varname in output_dict:
						output_dict[varname][fn]=a[k]
					else:
						output_dict[varname]={fn:a[k]}
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(output_dict,safe=False)
		else:
			print("failed\n+++++++")
			return JsonResponse({'status':'false','message':' | '.join(error_messages)}, status=400)