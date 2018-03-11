# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 11:48:28 2018

@author: ASUS-Laptop
"""
import json
import graphviz as gv

f = open("graph.json", "r")
graph = json.load(f)
f.close()

g = gv.Digraph(format='svg')

# nodes
nodes = []

for paper in graph:
    # nodes from graph
    nodes.append(paper)
    #nodes from cite
    for cite in graph[paper]['citations']:
        exist = False
        # filtert bekannte Paper
        if type(cite) == str:
            # überprüfe ob schon vorhanden
            for node in nodes:
                if node == cite:
                    exist = True
            if exist == False:
                nodes.append(cite)

    #nodes from ref
    for ref in graph[paper]['references']:
        exist = False
        # filtert bekannte Paper
        if type(ref) == str:
            # überprüfe ob schon vorhanden
            for node in nodes:
                if node == ref:
                    exist = True
            if exist == False:
                nodes.append(ref)
               
# edges
for paper in graph:
    for cite in graph[paper]['citations']:
        if type(cite)==str:
            g.edge(paper, cite)
    for ref in graph[paper]['references']:
        if type(ref)==str:
            g.edge(ref, paper)
        
g.render('img/g')

source = open('source.dot', 'w')
source.write(g.source)
source.close()

