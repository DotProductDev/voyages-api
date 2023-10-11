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
from common.nest import *
from common.reqs import *
from collections import Counter
from geo.common import GeoTreeFilter
from voyages3.localsettings import *


class EnslavedList(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
# 	serializer_class=EnslavedSerializer
	def options(self,request):
		j=options_handler('past/enslaved_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		st=time.time()
		times=[]
		labels=[]
		print("ENSLAVED LIST+++++++\nusername:",request.auth.user)
		print("FETCHING...")
# 		try:
		enslaved_options=options_handler('past/enslaved_options.json',hierarchical=False)
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
# 		except:
# 			return JsonResponse({'status':'false','message':'bad request'}, status=400)

class EnslavedTextFieldAutoComplete(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]				
	def post(self,request):
		print("+++++++\nusername:",request.auth.user)
# 		try:
		st=time.time()
		params=dict(request.POST)
		k=list(params.keys())[0]
		v=params[k][0]
		
		print("past/enslaved/autocomplete",k,v)
		queryset=Enslaved.objects.all()
		if '__' in k:
			kstub='__'.join(k.split('__')[:-1])
			k_id_field=kstub+"__id"
			queryset=queryset.prefetch_related(kstub)
		else:
			k_id_field="id"
		kwargs={'{0}__{1}'.format(k, 'icontains'):v}
		queryset=queryset.filter(**kwargs)
		queryset=queryset.order_by(k)
		total_results_count=queryset.count()
		candidates=[]
		candidate_vals=[]
		fetchcount=30
		## Have to use this ugliness b/c we're not in postgres
		## https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet.distinct
		for v in queryset.values_list(k_id_field,k).iterator():
			if v[1] not in candidate_vals:
				candidates.append(v)
				candidate_vals.append(v[1])
			if len(candidates)>=fetchcount:
				break
		res={
			"total_results_count":total_results_count,
			"results":[
				{
					"id":c[0],
					"label":c[1]
				} for c in candidates
			]
		}
		
		print("Internal Response Time:",time.time()-st,"\n+++++++")
		return JsonResponse(res,safe=False)

class EnslaverTextFieldAutoComplete(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		print("+++++++\nusername:",request.auth.user)
# 		try:
		st=time.time()
		params=dict(request.POST)
		params=dict(request.POST)
		k=list(params.keys())[0]
		v=params[k][0]
		
		print("past/enslavers/autocomplete",k,v)
		queryset=EnslaverIdentity.objects.all()
		if '__' in k:
			kstub='__'.join(k.split('__')[:-1])
			k_id_field=kstub+"__id"
			queryset=queryset.prefetch_related(kstub)
		else:
			k_id_field="id"
		kwargs={'{0}__{1}'.format(k, 'icontains'):v}
		queryset=queryset.filter(**kwargs)
		queryset=queryset.order_by(k)
		total_results_count=queryset.count()
		candidates=[]
		candidate_vals=[]
		fetchcount=30
		## Have to use this ugliness b/c we're not in postgres
		## https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet.distinct
		for v in queryset.values_list(k_id_field,k).iterator():
			if v[1] not in candidate_vals:
				candidates.append(v)
				candidate_vals.append(v[1])
			if len(candidates)>=fetchcount:
				break
		res={
			"total_results_count":total_results_count,
			"results":[
				{
					"id":c[0],
					"label":c[1]
				} for c in candidates
			]
		}
		print("Internal Response Time:",time.time()-st,"\n+++++++")
		return JsonResponse(res,safe=False)

#LONG-FORM TABULAR ENDPOINT.
class EnslaverList(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
# 	serializer_class=EnslaverSerializer
	def options(self,request):
		j=options_handler('past/enslaver_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		print("ENSLAVER LIST+++++++\nusername:",request.auth.user)# 
# 		try:
		st=time.time()
		enslaver_options=options_handler('past/enslaver_options.json',hierarchical=False)
		queryset=EnslaverIdentity.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,request,enslaver_options,auto_prefetch=True)
		if len(error_messages)==0:
			headers={"next_uri":next_uri,"prev_uri":prev_uri,"total_results_count":results_count}
			read_serializer=EnslaverSerializer(queryset,many=True)
			serialized=read_serializer.data
	
			outputs=[]
			outputs=serialized
			
			## now let's add some flattened enslavement relations
			
			
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(outputs,safe=False,headers=headers)
		else:
			return JsonResponse({'status':'false','message':' | '.join(error_messages)}, status=500)
# 		except:
# 			return JsonResponse({'status':'false','message':'bad request'}, status=400)



# Basic statistics
## takes a numeric variable
## returns its sum, average, max, min, and stdv
class EnslavedAggregations(generics.GenericAPIView):
# 	serializer_class=EnslavedSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		try:
			st=time.time()
			print("+++++++\nusername:",request.auth.user)
			params=dict(request.POST)
			aggregations=params.get('aggregate_fields')
			print("aggregations:",aggregations)
			queryset=Enslaved.objects.all()
			enslaved_options=options_handler('past/enslaved_options.json',hierarchical=False)
			aggregation,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,request,enslaved_options,retrieve_all=True)
			output_dict={}
			if len(error_messages)==0:
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
		except:
			return JsonResponse({'status':'false','message':'bad request'}, status=400)


# # Basic statistics
# ## takes a numeric variable
# ## returns its sum, average, max, min, and stdv
class EnslaverAggregations(generics.GenericAPIView):
# 	serializer_class=EnslaverSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		st=time.time()
		print("+++++++\nusername:",request.auth.user)
		try:
			enslaver_options=options_handler('past/enslaver_options.json',hierarchical=False)
			params=dict(request.POST)
			aggregations=params.get('aggregate_fields')
			print("aggregations:",aggregations)
			queryset=EnslaverIdentity.objects.all()
		
			aggregation,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,request,enslaver_options,retrieve_all=True)
			output_dict={}
			
			if len(error_messages)==0:
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
		except:
			return JsonResponse({'status':'false','message':'bad request'}, status=400)
			

class EnslavedDataFrames(generics.GenericAPIView):
# 	serializer_class=VoyageSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def options(self,request):
		j=options_handler('past/enslaved_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		print("+++++++\nusername:",request.auth.user)
		st=time.time()
		params=dict(request.POST)
		enslaved_options=options_handler('past/enslaved_options.json',hierarchical=False)
		queryset=Enslaved.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(
			queryset,
			self,
			request,
			enslaved_options,
			auto_prefetch=True,
			retrieve_all=True
		)
		queryset=queryset.order_by('id')
		sf=list(selected_fields)
		if len(error_messages)==0:
			output_dicts={}
			for s in sf:
				output_dicts[s]=[i[0] for i in queryset.values_list(s)]
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(output_dicts,safe=False)
		else:
			print("failed\n+++++++")
			print(' | '.join(error_messages))
			return JsonResponse({'status':'false','message':' | '.join(error_messages)}, status=400)

class EnslaverDataFrames(generics.GenericAPIView):
# 	serializer_class=VoyageSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def options(self,request):
		j=options_handler('past/enslaver_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		print("+++++++\nusername:",request.auth.user)
		st=time.time()
		params=dict(request.POST)
		enslaved_options=options_handler('past/enslaver_options.json',hierarchical=False)
		queryset=EnslaverIdentity.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(
			queryset,
			self,
			request,
			enslaved_options,
			auto_prefetch=True,
			retrieve_all=True
		)
		queryset=queryset.order_by('id')
		sf=list(selected_fields)
		if len(error_messages)==0:
			output_dicts={}
			for s in sf:
				output_dicts[s]=[i[0] for i in queryset.values_list(s)]
			print("Internal Response Time:",time.time()-st,"\n+++++++")
			return JsonResponse(output_dicts,safe=False)
		else:
			print("failed\n+++++++")
			print(' | '.join(error_messages))
			return JsonResponse({'status':'false','message':' | '.join(error_messages)}, status=400)


class EnslaverGeoTreeFilter(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def options(self,request):
		j=options_handler('past/enslaver_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		print("Enslaved Geo Tree+++++++\nusername:",request.auth.user)
		st=time.time()
		reqdict=dict(request.POST)
		enslaver_options=options_handler('past/enslaver_options.json',hierarchical=False)
		geotree_valuefields=reqdict['geotree_valuefields']
		del(reqdict['geotree_valuefields'])
		queryset=EnslaverIdentity.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,reqdict,enslaver_options,retrieve_all=True)
		for geotree_valuefield in geotree_valuefields:
			geotree_valuefield_stub='__'.join(geotree_valuefield.split('__')[:-1])
			queryset=queryset.select_related(geotree_valuefield_stub)
		vls=[]
		for geotree_valuefield in geotree_valuefields:		
			vls+=[i[0] for i in list(set(queryset.values_list(geotree_valuefield))) if i[0] is not None]
		vls=list(set(vls))
# 		print(len(vls),"filtered vals")
# 		print("first 10:",vls[:10])
		filtered_geotree=GeoTreeFilter(spss_vals=vls)
		resp=JsonResponse(filtered_geotree,safe=False)
		print("Internal Response Time:",time.time()-st,"\n+++++++")
		return resp


class EnslavedGeoTreeFilter(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def options(self,request):
		j=options_handler('past/enslaved_options.json',request)
		return JsonResponse(j,safe=False)
	def post(self,request):
		print("Enslaved Geo Tree+++++++\nusername:",request.auth.user)
		st=time.time()
		reqdict=dict(request.POST)
		enslaved_options=options_handler('past/enslaved_options.json',hierarchical=False)
		geotree_valuefields=reqdict['geotree_valuefields']
		del(reqdict['geotree_valuefields'])
		queryset=Enslaved.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(queryset,self,reqdict,enslaved_options,retrieve_all=True)
		for geotree_valuefield in geotree_valuefields:
			geotree_valuefield_stub='__'.join(geotree_valuefield.split('__')[:-1])
			queryset=queryset.select_related(geotree_valuefield_stub)
		vls=[]
		for geotree_valuefield in geotree_valuefields:		
			vls+=[i[0] for i in list(set(queryset.values_list(geotree_valuefield))) if i[0] is not None]
		vls=list(set(vls))
# 		print(len(vls),"filtered vals")
# 		print("first 10:",vls[:10])
		filtered_geotree=GeoTreeFilter(spss_vals=vls)
		resp=JsonResponse(filtered_geotree,safe=False)
		print("Internal Response Time:",time.time()-st,"\n+++++++")
		return resp


class EnslavedAggRoutes(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		st=time.time()
		print("+++++++\nusername:",request.auth.user)
		params=dict(request.POST)
		enslaved_options=options_handler('past/enslaved_options.json',hierarchical=False)
		queryset=Enslaved.objects.all()
		queryset,selected_fields,next_uri,prev_uri,results_count,error_messages=post_req(
			queryset,
			self,
			request,
			enslaved_options,
			auto_prefetch=True,
			retrieve_all=True
		)
		
		zoomlevel=params.get('zoomlevel',['region'])[0]
				
		if zoomlevel not in ['region','place']:
			zoomlevel='region'
		if zoomlevel=='place':
			enslaved_values_list=queryset.values_list(
				'language_group__uuid',
				'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__uuid',
				'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__uuid',
				'post_disembark_location__geo_location__uuid'
			)
			graphname='place'
		elif zoomlevel=='region':
			enslaved_values_list=queryset.values_list(
				'language_group__uuid',
				'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__uuid',
				'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__uuid',
				'post_disembark_location__geo_location__uuid'
			)
			graphname='region'
			
# 		print("VALUES LIST",enslaved_values_list)
		
		counter=Counter(list(enslaved_values_list))
		counter2={"__".join([str(i) for i in c]):counter[c] for c in counter}
		
		django_query_time=time.time()
		print("Internal Django Response Time:",django_query_time-st,"\n+++++++")
		
		u2=GEO_NETWORKS_BASE_URL+'network_maps/'
		d2={
			'graphname':graphname,
			'cachename':'ao_maps',
			'payload':counter2,
			'linklabels':['origination','transportation','disposition'],
			'nodelabels':[
				'origin',
				'embarkation',
				'disembarkation',
				'post-disembarkation'
			]
		}
		
		
		
		r=requests.post(url=u2,data=json.dumps(d2),headers={"Content-type":"application/json"})
		print("Networkx Response Time Back to Django:", time.time()-django_query_time)
		j=json.loads(r.text)
		
		print("Total Internal Response Time:",time.time()-st,"\n+++++++")
		return JsonResponse(j,safe=False)


class PASTNetworks(generics.GenericAPIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	def post(self,request):
		st=time.time()
		print("+++++++\nusername:",request.auth.user)
		params=json.dumps(dict(request.POST))
		print(PEOPLE_NETWORKS_BASE_URL)
		r=requests.post(PEOPLE_NETWORKS_BASE_URL,data=params,headers={"Content-type":"application/json"})
		j=json.loads(r.text)
		return JsonResponse(j,safe=False)

		



