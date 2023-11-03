from math import sqrt
import networkx as nx
from localsettings import *
import requests
import json
import itertools
from networkx_query import search_nodes, search_edges
import uuid
import time


def load_graph():
	url=DJANGO_BASE_URL+'common/past_graph/'
	headers={'Authorization':DJANGO_AUTH_KEY,'Content-Type': 'application/json'}
	
	G=nx.Graph()
	
	r=requests.post(
		url=url,
		headers=headers
	)
	
	j=json.loads(r.text)
	
# STRUCTURE	
# 		relation_map={
# 			'enslaved':enslaved_people_df,
# 			'enslavers':enslaver_aliases_df,
# 			'voyages':voy_df,
# 			'enslavement_relations':enslavementrelation_df,
# 			'enslaved_in_relation':enslaved_in_relation_df,
# 			'enslavers_in_relation':enslaver_in_relation_df	
# 		}
	
	idmap={
		'enslaved':{},
		'enslavers':{},
		'voyages':{},
		'enslavement_relations':{}
	}
	
	#currently, enslaver aliases are "in front" of enslaver identities
	#which means we need the aliases to connect identities to relations
	#but also that we get duplicate identities back
	enslaver_alias_map={}
	
	for dfname in ['enslaved','enslavers','voyages','enslavement_relations']:
		df=j[dfname]
		for row_idx in range(len(df['id'])):
			id=df['id'][row_idx]
			uid=str(uuid.uuid4())
			
			#currently, enslaver aliases are "in front" of enslaver identities
			#which means we need the aliases to connect identities to relations
			#but also that we get duplicate identities back
			if dfname=='enslavers':
				alias_id=df['alias_id'][row_idx]
				enslaver_alias_map[alias_id]=id
				if id in idmap[dfname]:
					#wanted to retain the alias ids but this is slow as hell.
					#an alternative method would be to add an extra dataframe call connecting aliases to identities
					#but i don't see the value here as we can always get the aliases on a call to the identity-based enslaver list endpoint
					
					# enslaver_node_id=[n for n in 
# 						search_nodes(G, {"==": [('id',), id]})
# 					][0]
# 					enslaver_node=G.nodes[enslaver_node_id]
# 					print("APPENDING",id,enslaver_node)
# 					enslaver_node['alias_ids'].append(alias_id)
					pass
				else:
# 					print("adding",id)
					idmap[dfname][id]=uid
					alias_ids=[alias_id]
					obj={k:df[k][row_idx] for k in list(df.keys()) if k!= 'alias_id'}
# 					obj['alias_ids']=alias_ids
					obj['node_class']=dfname
					obj['uuid']=uid
					G.add_node(uid, **obj)
			else:
				idmap[dfname][id]=uid
				obj={k:df[k][row_idx] for k in list(df.keys())}
				obj['node_class']=dfname
				obj['uuid']=uid
				G.add_node(uid, **obj)
	
	eir = j['enslaved_in_relation']
	for row_idx in range(len(eir['relation'])):
		obj={k:eir[k][row_idx] for k in list(eir.keys())}
		enslaved_uuid=idmap['enslaved'][obj['enslaved']]
		relation_uuid=idmap['enslavement_relations'][obj['relation']]
		G.add_edge(enslaved_uuid,relation_uuid)
	
	eir = j['enslavers_in_relation']
	for row_idx in range(len(eir['relation'])):
		obj={k:eir[k][row_idx] for k in list(eir.keys())}
		#currently, enslaver aliases are "in front" of enslaver identities
		#which means we need the aliases to connect identities to relations
		#but also that we get duplicate identities back
		identity_id=enslaver_alias_map[obj['enslaver_alias']]
		enslaver_uuid=idmap['enslavers'][identity_id]
		relation_uuid=idmap['enslavement_relations'][obj['relation']]
		G.add_edge(enslaver_uuid,relation_uuid,roles__name=obj['roles__name'])
	
	#then once more around to get voyages tied in to relations
	enslavement_relations=[n for n in 
		search_nodes(G, {"==": [('node_class',), 'enslavement_relations']})
	]
	
	for n_id in enslavement_relations:
		voyage_id=G.nodes[n_id]['voyage']
		if voyage_id is not None:
			voyage_uuid=idmap['voyages'][voyage_id]
			G.add_edge(n_id,voyage_uuid)
	
	#let's try to purge unnecessary enslavement relation intermediary nodes
	#specifically, nodes where we have only enslavers tied to voyages, and no enslaved people tied to these relations
	#those should just be treated as pass-throughs
	
	transportation_relations=[n for n in 
		search_nodes(G, {
			'and': [
				{"==": [('node_class',), 'enslavement_relations']},
				{"==": [('relation_type__name',), 'Transportation']}
			]	
		})
	]
	
	nodes_to_delete=[]
	
	print("graph before disintermediating\n\
1) investor/captain-->voyage cnx's\n\
2) enslaved-->voyage cnx's when no shipper, consignor, etc. is present:\n",G,'\n----')
	
	for n in transportation_relations:
		edges=G.edges(n,data=True)
		has_enslaved=False
		has_direct_enslavers=False
		has_indirect_enslavers=False
		other_node_ids=[]
		for edge in edges:
			s,t,edata=edge
			if s==n:
				other=t
			else:
				other=s
			if other is not None:
				other_node_ids.append(other)
			if G.nodes[other]['node_class']=='enslaved':
				has_enslaved=True
			if G.nodes[other]['node_class']=='enslavers' and 'roles__name' in edata:
				if edata['roles__name'] not in ['Investor','Captain']:
					has_direct_enslavers=True
				else:
					has_indirect_enslavers=True
		if (not has_enslaved and has_indirect_enslavers) or (not has_direct_enslavers and has_enslaved):
			
			nodes_to_delete.append(n)
			for pair in itertools.permutations(other_node_ids,2):
				a,b=pair
				anode=G.nodes[a]
				bnode=G.nodes[b]
				skipthis=False
				if anode['node_class']=='voyages':
					s=b
					t=a
					snodeclass=bnode['node_class']
				elif bnode['node_class']=='voyages':
					s=a
					t=b
					snodeclass=anode['node_class']
				else:
					# in this case, we're getting
					## two enslavers or enslaved connected to the same relation
					# we don't want to link them directly -- but rather through the voyage
					skipthis=True
				if not skipthis:
					if has_indirect_enslavers and snodeclass=='enslavers':
						#in this case, we have an enslaver-to-voyage connection to make
						roles_name=G.edges[s,n]['roles__name']
						G.add_edge(s,t,role_name=roles_name)
					if has_enslaved:
						G.add_edge(s,t)
		
	nodes_to_delete=list(set(nodes_to_delete))
	
	for n in nodes_to_delete:
		G.remove_node(n)
	print("pruned, final graph: ",G)
	return G



def add_neighbors(G,nodes_dict,n,edges_list,levels=1):
	edges=G.edges(n,data=True)
	selfdata=G.nodes[n]
	if levels>0:
		for edge in edges:
			s,t,edata=edge
			
			if s==n:
				other=t
			else:
				other=s
			otherdata=G.nodes[other]
			other_node_class=otherdata['node_class']
			if other_node_class=='enslavement_relations':
				nodes_dict,edges_list=add_neighbors(G,nodes_dict,other,edges_list,levels=levels)
			else:
				nodes_dict,edges_list=add_neighbors(G,nodes_dict,other,edges_list,levels=levels-1)
			s,t=sorted([s,t])
			e={'source':s,'target':t,'data':edata}
			if e not in edges_list:
				edges_list.append(e)
			nodes_dict[other]=otherdata
	nodes_dict[n]=selfdata
	return(nodes_dict,edges_list)


## The below recursive functions were attempts to screen out the enslavement relation intermediary nodes after the fact but I had to abandon them for the sake of time
# def add_successors(G,nodes_dict,n,edges,prior_id=None):
# 	passthrough_node_classes=['enslavement_relations']
# 	successors=G.successors(n)
# # 	print("add successors to",n)
# 	for s in successors:
# 		sdata=G.nodes[s]
# # 		print("s:",s,json.dumps(sdata,indent=2))
# 		print(n,"--has successor-->",s,sdata)
# 		if sdata['node_class'] in passthrough_node_classes:
# 			nodes_dict,edges=add_predecessors(G,nodes_dict,s,edges,prior_id=n)
# 			nodes_dict,edges=add_successors(G,nodes_dict,s,edges,prior_id=n)
# 		else:
# 			if prior_id is None:
# 				thisnode_id=n
# 				prior_edata={}
# 			else:
# 				thisnode_id=prior_id
# 				try:
# 					next_edata=G.edges[n,s]
# 				except:
# 					next_edata=G.edges[s,n]
# 			#avoid self-loops and unnecessary interconnections
# 			#unfortunately, this move does screen out
# 			## spousal relations between enslavers
# 			## mutual transaction relations between enslaved (i.e., bought/sold by the same enslaver on the same vessel)
# 			thisnodedata=G.nodes[thisnode_id]
# 			if thisnode_id != s and thisnodedata['node_class']!=sdata['node_class']:
# 				nodes_dict[thisnode_id]=G.nodes[thisnode_id]
# 				try:
# 					this_edata=G.edges[thisnode_id,n]
# 				except:
# 					this_edata=G.edges[n,thisnode_id]
# 				merged_edata=this_edata|next_edata
# 				e={'source':thisnode_id,'target':s,'data':merged_edata}
# 				if e not in edges:
# 					edges.append(e)
# 				nodes_dict[s]=G.nodes[s]
# 	return nodes_dict,edges
# 
# def add_predecessors(G,nodes_dict,n,edges,prior_id=None):
# 	passthrough_node_classes=['enslavement_relations']
# 	predecessors=G.predecessors(n)
# # 	print("add predecessors to",n)
# 	for p in predecessors:
# 		pdata=G.nodes[p]
# # 		print("p:",p,json.dumps(pdata,indent=2))
# 		print(n,'--has predecessor-->',p,pdata)
# 		if pdata['node_class']==['enslavement_relations'] in passthrough_node_classes:
# 			nodes_dict,edges=add_predecessors(G,nodes_dict,p,edges,prior_id=n)
# 			nodes_dict,edges=add_successors(G,nodes_dict,p,edges,prior_id=n)
# 		else:
# 			if prior_id is None:
# 				thisnode_id=n
# 				prior_edata={}
# 			else:
# 				thisnode_id=prior_id
# 				try:
# 					prior_edata=G.edges[p,n]
# 				except:
# 					prior_edata=G.edges[n,p]
# 			thisnodedata=G.nodes[thisnode_id]
# 			#avoid self-loops and unnecessary interconnections
# 			#unfortunately, this move does screen out
# 			## spousal relations between enslavers
# 			## mutual transaction relations between enslaved (i.e., bought/sold by the same enslaver on the same vessel)
# 			if thisnode_id!=p and thisnodedata['node_class']!=pdata['node_class']:
# 				nodes_dict[thisnode_id]=G.nodes[thisnode_id]
# 				try:
# 					this_edata=G.edges[n,thisnode_id]
# 				except:
# 					this_edata=G.edges[thisnode_id,n]
# 				merged_edata=prior_edata|this_edata
# 				e={'source':p,'target':thisnode_id,'data':merged_edata}
# 				if e not in edges:
# 					edges.append(e)
# 				nodes_dict[p]=G.nodes[p]
# 	return nodes_dict,edges