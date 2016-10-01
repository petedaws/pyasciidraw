import math
import ascii_layout
import force_directed

try:
	edges.append((nodes[0],nodes[1]))
	edges.append((nodes[1],nodes[2]))
	edges.append((nodes[0],nodes[2]))
	edges.append((nodes[0],nodes[3]))
except:
	pass
	
nodes = {}
for i,node in enumerate(range(10)):
	node = {}
	node['id'] = i
	node['label'] = str(i)
	node['x'] = 0.01*math.cos(i)
	node['y'] = 0.01*math.sin(i)
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

def layout(nodes,edges):
	for i in range(2000):
		force_directed.init_force(nodes)
		force_directed.node_repulsion(nodes)
		force_directed.edge_attraction(edges)
		force_directed.force_limit(nodes)
		force_directed.propogate(nodes)

canvas = ascii_layout.create_canvas(50,50)
layout(nodes,edges)
force_directed.translate(nodes,25,25)
for node,o_node in edges:
	ascii_layout.drawline(canvas,'.',(int(node['x']),int(node['y'])),(int(o_node['x']),int(o_node['y'])))
for node in nodes.values():
	ascii_layout.drawtextbox(canvas,str(node['label']),(int(node['x']),int(node['y'])))
ascii_layout.drawcorrect(canvas)

