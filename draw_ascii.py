import math
from ascii_layout import Canvas
import force_directed

graph1 = [
		('aa44','bb65'),
		('cc23','dd23'),
		('cc23','bb65'),
		('cc13','bb25'),
		('aa44','bb25'),
		('cc13','dd23'),
		('bb65','1234'),
		('1234','aa55'),
		('1274','ax55'),
		('1274','bb25'),
		]

def translate_positive(nodes):
	extreme = force_directed.get_extremes(nodes)
	translatex = abs(extreme[0])+10
	translatey = abs(extreme[1])+4
	force_directed.translate(nodes,translatex,translatey)

canvas = Canvas()
nodes,edges = force_directed.parse_edge_list(graph1)
force_directed.layout(nodes,edges,2000)
translate_positive(nodes)

for node,o_node in edges:
	canvas.drawline('.',(int(node['x']),int(node['y'])),(int(o_node['x']),int(o_node['y'])))
for node in nodes.values():
	print('node',str(node['label']),(int(node['x']),int(node['y'])))
	canvas.drawtextbox(str(node['label']),(int(node['x']),int(node['y'])))
canvas.draw()

