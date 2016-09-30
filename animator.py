import math
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import networkx as nx
import force_directed


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

G = nx.Graph()
def init():
	G.add_nodes_from(nodes.keys())
	G.add_edges_from([(c['id'],d['id']) for c,d in edges])
	return []

def animate(i):
	force_directed.init_force(nodes)
	force_directed.node_repulsion(nodes)
	force_directed.edge_attraction(edges)
	force_directed.force_limit(nodes)
	force_directed.propogate(nodes)
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
