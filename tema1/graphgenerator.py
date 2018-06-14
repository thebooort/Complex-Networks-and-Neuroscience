#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:16:07 2018

@author: booort
"""
#import libraries
import networkx as nx
import matplotlib.pyplot as plt

#for loop for printing and save all graphs generated
for i in range(1,9):
    G=nx.complete_graph(i)
    nx.draw_networkx(G)
    plt.show()
    plt.savefig('grafo_completo_grado_%i.png'%(i))
    
#I've used networkx library, de code that generate the graph is:
    """
    def complete_graph(n,create_using=None):
    ###
    Return the complete graph K_n with n nodes.

    Node labels are the integers 0 to n-1.
    ###
    G=empty_graph(n,create_using)
    G.name="complete_graph(%d)"%(n)
    if n>1:
        if G.is_directed():
            edges=itertools.permutations(range(n),2)
        else:
            edges=itertools.combinations(range(n),2)
        G.add_edges_from(edges)
    return G
    """
    