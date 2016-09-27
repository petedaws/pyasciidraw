import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation
import random

RCONST = 1
SCONST = 0.1

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 50), ylim=(0, 50))

nodes = {}
for i,node in enumerate(range(10)):
	node = {}
	node['id'] = i
	node['x'] = 25+random.random()
	node['y'] = 25+random.random()
	nodes[i] = node

edges = []
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

def force_repulsion(nodes):
	for node in nodes.values():
		node['fx'] = 0
		node['fy'] = 0
		for o_node in nodes.values():
			xdistance = node['x'] - o_node['x']
			ydistance = node['y'] - o_node['y']
			distance = math.sqrt((xdistance)**2+(ydistance)**2)
			angle = math.atan2(ydistance,xdistance)
			xunit = math.cos(angle)
			yunit = math.sin(angle)
			if node['id'] == o_node['id']:
				continue
			try:
				node['fx'] = node['fx'] + RCONST*1/(distance**2)*xunit
				node['fy'] = node['fy'] + RCONST*1/(distance**2)*yunit
			except ZeroDivisionError:
				pass
				

def string_attraction(edges):
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

def init():
	return []

	
def animate(i):
	ann = []
	for node in nodes.values():
		force_repulsion(nodes)
		string_attraction(edges)
		node['x'] = node['x'] + node['fx']
		node['y'] = node['y'] + node['fy']
		ann.append(plt.annotate(str(node['id']), xy=(node['x'],node['y'])))
	return ann
	
anim = animation.FuncAnimation(fig, animate, 
							   init_func=init, 
							   frames=360, 
							   interval=20,
							   blit=True)

plt.show()
