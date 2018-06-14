#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:32:23 2018

@author: booort
"""

import networkx as nx
import random as rn
import matplotlib.pyplot as plt

#number of steps
run_time=100000

#variables for de B-A graph creation, and graoh creation
nodes=100
edges=3
probability=1
population=nx.watts_strogatz_graph(nodes,edges,probability)

#We set all nodes with 'r' variable and print a summary for our graph
nx.set_node_attributes(population,'r','partido')
print(nx.info(population))

#visual representaiton
nx.draw(population)
plt.show()

#We randomize the partido variable between nodes
changed_nodes=[]
not_changed=[]
for i in range(len(population.nodes())):
    aux=rn.randrange(0,2,1)
    if aux==1:
        population.node[i]['partido']='b'
        changed_nodes.append(i)
    else:
        not_changed.append(i)

#visual representation after the randomize        
   # we get the position of the nodes
pos=nx.spring_layout(population)
nx.draw_networkx_nodes(population,pos,
                       nodelist=changed_nodes,
                       node_color='b',
                       node_size=100,
                   alpha=0.8)
nx.draw_networkx_nodes(population,pos,
                       nodelist=not_changed,
                       node_color='r',
                       node_size=100,
                   alpha=0.8)     
nx.draw_networkx_edges(population,pos,width=1.0,alpha=0.5)
plt.show()
print('Inicialmente tenemos {} azules y {} rojos'.format(len(changed_nodes),len(not_changed)))

#main part: we execute voter model 'run_time' times
vector_proporcion=[]
for i in range(run_time):
    node_influencer=rn.randrange(0, nodes-1,1)     
    node_receiver=list(population.neighbors(node_influencer))[rn.randrange(0, len(list(population.neighbors(node_influencer))),1)]
    if population.node[node_influencer]['partido']!=population.node[node_receiver]['partido']:
        if population.node[node_influencer]['partido']=='r':
            population.node[node_receiver]['partido']='r'
        else:
            population.node[node_receiver]['partido']='b'
    result_changed=[]
    result_not_changed=[]
    for j in range(len(population.nodes())):
        if population.node[j]['partido']=='b':
            result_changed.append(j)
        else:
            result_not_changed.append(j)
    vector_proporcion.append(len(result_changed)/len(result_not_changed))


#visual representation of the resfult

pos=nx.spring_layout(population)
nx.draw_networkx_nodes(population,pos,
                       nodelist=result_changed,
                       node_color='b',
                       node_size=100,
                   alpha=0.8)
nx.draw_networkx_nodes(population,pos,
                       nodelist=result_not_changed,
                       node_color='r',
                       node_size=100,
                   alpha=0.8)     
nx.draw_networkx_edges(population,pos,width=1.0,alpha=0.5)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(vector_proporcion)
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()