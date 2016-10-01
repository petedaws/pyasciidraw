import math
import random

RCONST = 6
SCONST = 0.01
MAXFORCE = 1

def init_force(nodes):
	for node in nodes.values():
		node['fx'] = 0
		node['fy'] = 0

def node_repulsion(nodes):
	for node in nodes.values():
		for o_node in nodes.values():
			if node['id'] == o_node['id']:
				continue
			xdistance = node['x'] - o_node['x']
			ydistance = node['y'] - o_node['y']
			distance = math.sqrt((xdistance)**2+(ydistance)**2)
			angle = math.atan2(ydistance,xdistance)
			xunit = math.cos(angle)
			yunit = math.sin(angle)
			try:
				node['fx'] = node['fx'] + RCONST/(distance**2)*xunit
				node['fy'] = node['fy'] + RCONST/(distance**2)*yunit
			except ZeroDivisionError:
				pass
				

def edge_attraction(edges):
	for node,o_node in edges: 
		xdistance = node['x'] - o_node['x']
		ydistance = node['y'] - o_node['y']
		distance = math.sqrt((xdistance)**2+(ydistance)**2)
		angle = math.atan2(ydistance,xdistance)
		xunit = math.cos(angle)*distance
		yunit = math.sin(angle)*distance
		node['fx'] = node['fx'] - SCONST*xunit
		node['fy'] = node['fy'] - SCONST*yunit
		o_node['fx'] = o_node['fx'] + SCONST*xunit
		o_node['fy'] = o_node['fy'] + SCONST*yunit
		
def force_limit(nodes):
	for node in nodes.values():
		if abs(node['fx']) > MAXFORCE:
			node['fx'] = MAXFORCE * node['fx']/abs(node['fx'])
			
		if abs(node['fy']) > MAXFORCE:
			node['fy'] = MAXFORCE * node['fy']/abs(node['fy'])
			 
			 
def propogate(nodes):
	for node in nodes.values():
		node['x'] = node['x'] + node['fx']
		node['y'] = node['y'] + node['fy']
		
def translate(nodes,x,y):
	for node in nodes.values():
		node['x'] = node['x'] + x
		node['y'] = node['y'] + y

			
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
			new_node['x'] = random.randrange(-100,100)
			new_node['y'] = random.randrange(-100,100)
			nodes[new_node['id']] = new_node
		edges.append((nodes[edge_nodes[0]],nodes[edge_nodes[1]]))
	return nodes,edges
	
def get_center(nodes):
	sumx = 0
	sumy = 0
	for node in nodes.values():
		sumx += node['x']
		sumy += node['y']
	return (sumx/len(nodes),sumy/len(nodes))
