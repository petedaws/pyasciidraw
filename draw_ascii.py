import math
from ascii_layout import Canvas
import force_directed

graph1 = [
		('aa44','bb65'),
		('cc23','dd23'),
		('aa44','dd23'),
		('cc23','bb65'),
		('cc13','bb25'),
		('aa44','bb25'),
		('cc13','dd23'),
		('bb65','1234'),
		('1234','aa55'),
		]

def layout(nodes,edges):
	for i in range(2000):
		force_directed.init_force(nodes)
		force_directed.node_repulsion(nodes)
		force_directed.edge_attraction(edges)
		force_directed.force_limit(nodes)
		force_directed.propogate(nodes)
		
def translate_to_center(nodes,xmax,ymax):
	center = force_directed.get_center(nodes)
	translatex = float(xmax)/2-center[0]
	translatey = float(ymax)/2-center[1]
	force_directed.translate(nodes,translatex,translatey)

canvas = Canvas(50,50)
nodes,edges = force_directed.parse_edge_list(graph1)
layout(nodes,edges)
translate_to_center(nodes,50,50)

for node,o_node in edges:
	canvas.drawline('.',(int(node['x']),int(node['y'])),(int(o_node['x']),int(o_node['y'])))
for node in nodes.values():
	canvas.drawtextbox(str(node['label']),(int(node['x']),int(node['y'])))
canvas.draw()

