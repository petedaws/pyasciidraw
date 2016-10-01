import math
import ascii_layout
import force_directed
import random


graph1 = [
		('a','b'),
		('c','d'),
		('a','d'),
		('c','b'),
		]
			
# Take in a list of string tuples
def parse_edge_list(graph):
	nodes = {}
	edges = []
	for edge_nodes in graph:
		for node in edge_nodes:
			if node in nodes:
				continue
			new_node = {}
			new_node['id'] = node
			new_node['label'] = str(node)
			new_node['x'] = 0.01*random.random()
			new_node['y'] = 0.01*random.random()
			nodes[new_node['id']] = new_node
		edges.append((nodes[edge_nodes[0]],nodes[edge_nodes[1]]))
	return nodes,edges

def layout(nodes,edges):
	for i in range(2000):
		force_directed.init_force(nodes)
		force_directed.node_repulsion(nodes)
		force_directed.edge_attraction(edges)
		force_directed.force_limit(nodes)
		force_directed.propogate(nodes)

canvas = ascii_layout.create_canvas(50,50)
nodes,edges = parse_edge_list(graph1)
layout(nodes,edges)
force_directed.translate(nodes,25,25)
for node,o_node in edges:
	ascii_layout.drawline(canvas,'.',(int(node['x']),int(node['y'])),(int(o_node['x']),int(o_node['y'])))
for node in nodes.values():
	ascii_layout.drawtextbox(canvas,str(node['label']),(int(node['x']),int(node['y'])))
ascii_layout.drawcorrect(canvas)

