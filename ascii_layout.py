import math



def drawdot(canvas,pos):
	canvas[pos[1]][pos[0]] = '+'


def drawsquare(canvas,center,size):

	#top line
	drawdot(canvas,(center[0]-size,center[1]+size))
	drawdot(canvas,(center[0]+size,center[1]+size))
	drawline(canvas,'-',center[0]-size,center[1]+size,center[0]+size,center[1]+size)

	#bottom line
	drawdot(canvas,(center[0]-size,center[1]-size))
	drawdot(canvas,(center[0]+size,center[1]-size))
	drawline(canvas,'-',center[0]-size,center[1]-size,center[0]+size,center[1]-size)

	#left line
	drawline(canvas,'|',center[0]-size,center[1]-size,center[0]-size,center[1]+size)

	#right line
	drawline(canvas,'|',center[0]+size,center[1]-size,center[0]+size,center[1]+size)

def drawrect(canvas,bottomleft,topright):

	bottomright = (topright[0],bottomleft[1])
	topleft = (bottomleft[0], topright[1])

	#top line
	drawdot(canvas,topleft)
	drawdot(canvas,topright)
	drawline(canvas,'-',topleft,topright)

	#bottom line
	drawdot(canvas,bottomleft)
	drawdot(canvas,bottomright)
	drawline(canvas,'-',bottomleft,bottomright)

	#left line
	drawline(canvas,'|',topleft,bottomleft)

	#right line
	drawline(canvas,'|',topright,bottomright)

def drawtext(canvas,text,pos):
	for i,char in enumerate(text):
		 canvas[pos[1]][pos[0]+i] = char

def drawtextbox(canvas,text,pos):

	bottomleft = (pos[0]-1,pos[1]-1)
	topright = (pos[0] + len(text), pos[1]+1)
	drawrect(canvas,bottomleft,topright)
	drawtext(canvas,text,pos)

def create_canvas(x,y):
	output = []
	for a in range(y):
		line = []
		for b in range(x):
			line.append(' ')
		output.append(line)
	return output

def draw(canvas,draw_axis=False):
	if draw_axis:
		xaxis = [str(x % 10) for x in range(len(canvas[0]))]
	else:
		xaxis = []
	xaxis.insert(0,' ')
	output = []
	output.insert(0,''.join(xaxis))
	for i,line in enumerate(canvas):
		if draw_axis:
			line.insert(0,str(i%10))
		output.insert(0,''.join(line))

	for line in output:
		print(line)

def drawline(canvas,style,start,end):
	angle = math.atan2(float(end[1]-start[1]),float(end[0]-start[0]))
	pos = start
	while True:
		pos = (pos[0]+math.cos(angle),pos[1]+math.sin(angle))
		if abs(pos[0]-end[0]) < 1 and abs(pos[1]-end[1]) < 1:
			break
		canvas[math.floor(pos[1])][math.floor(pos[0])] = style
