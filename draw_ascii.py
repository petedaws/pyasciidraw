import math
import ascii_layout

nodes = {}
for i,node in enumerate(range(3)):
	node = {}
	node['id'] = i
	node['label'] = str(i)
	node['x'] = 5+0.01*math.cos(i)
	node['y'] = 5+0.01*math.sin(i)
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

canvas = ascii_layout.create_canvas(10,10)
for node in nodes.values():
	x = int(node['x'])
	y = int(node['y'])
	ascii_layout.drawtext(canvas,str(node['id']),(x,y))
	
ascii_layout.drawcorrect(canvas)

