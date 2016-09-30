import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import networkx as nx

RCONST = 1
SCONST = 0.1
MAXFORCE = 1

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))

nodes = {}
for i,node in enumerate(range(10)):
	node = {}
	node['id'] = i
	node['label'] = str(i)
	node['x'] = random.random()
	node['y'] = random.random()
	nodes[i] = node

edges = []


try:
	edges.append((nodes[0],nodes[1]))
	edges.append((nodes[1],nodes[2]))
	edges.append((nodes[2],nodes[3]))
	edges.append((nodes[3],nodes[4]))
	edges.append((nodes[4],nodes[5]))
	edges.append((nodes[5],nodes[6]))
	edges.append((nodes[3],nodes[7]))
	edges.append((nodes[5],nodes[8]))
	edges.append((nodes[1],nodes[9]))
	edges.append((nodes[0],nodes[6]))
	edges.append((nodes[0],nodes[3]))
except:
	pass

def init_force(nodes):
	for node in nodes.values():
		node['fx'] = 0
		node['fy'] = 0

def force_repulsion(nodes):
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

G = nx.Graph()
def init():
	G.add_nodes_from(nodes.keys())
	G.add_edges_from([(c['id'],d['id']) for c,d in edges])
	return []

def animate(i):
	init_force(nodes)
	force_repulsion(nodes)
	edge_attraction(edges)
	force_limit(nodes)
	propogate(nodes)
	pos_nx = {}
	ann = []
	for node,pos in nodes.items():
		pos_nx[node] = (pos['x'],pos['y'])
	nns = nx.draw_networkx_nodes(G,pos=pos_nx)
	ees = nx.draw_networkx_edges(G,pos=pos_nx)
	return ees,nns
	
anim = animation.FuncAnimation(fig, animate, 
							   init_func=init, 
							   frames=360, 
							   interval=20,
							   blit=True)

plt.show()
