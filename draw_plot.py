from matplotlib import pyplot as plt
from matplotlib import animation
import networkx as nx
import force_directed
import math

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))

nodes = {}
for i,node in enumerate(range(3)):
	node = {}
	node['id'] = i
	node['label'] = str(i)
	node['x'] = 0+0.01*math.cos(i)
	node['y'] = 0+0.01*math.sin(i)
	nodes[i] = node

edges = []

try:
	edges.append((nodes[0],nodes[1]))
	edges.append((nodes[1],nodes[2]))
	edges.append((nodes[0],nodes[2]))
except:
	pass

def layout(nodes,edges):
	for i in range(200):
		force_directed.init_force(nodes)
		force_directed.node_repulsion(nodes)
		force_directed.edge_attraction(edges)
		force_directed.force_limit(nodes)
		force_directed.propogate(nodes)

G = nx.Graph()
G.add_nodes_from(nodes.keys())
G.add_edges_from([(c['id'],d['id']) for c,d in edges])

layout(nodes,edges)
pos_nx = {}
for node,pos in nodes.items():
	pos_nx[node] = (pos['x'],pos['y'])
nns = nx.draw_networkx(G,pos=pos_nx)
plt.show()
