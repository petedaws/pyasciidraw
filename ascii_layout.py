import math

class Canvas:
	def __init__(self,x,y):
		self.canvas = []
		for a in range(y):
			line = []
			for b in range(x):
				line.append(' ')
			self.canvas.append(line)
		
	def __insert(self,x,y,char):
		try:
			self.canvas[x][y] = char
		except IndexError:
			pass

	def drawdot(self,pos):
		self.__insert(pos[1],pos[0],'+')

	def drawsquare(self,center,size):

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

	def drawrect(self,bottomleft,topright):

		bottomright = (topright[0],bottomleft[1])
		topleft = (bottomleft[0], topright[1])

		#top line
		self.drawdot(topleft)
		self.drawdot(topright)
		self.drawline('-',topleft,topright)

		#bottom line
		self.drawdot(bottomleft)
		self.drawdot(bottomright)
		self.drawline('-',bottomleft,bottomright)

		#left line
		self.drawline('|',topleft,bottomleft)

		#right line
		self.drawline('|',topright,bottomright)

	def drawtext(self,text,pos):
		for i,char in enumerate(text):
			 self.__insert(pos[1],pos[0]+i,char)

	def drawtextbox(self,text,pos):

		bottomleft = (pos[0]-1,pos[1]-1)
		topright = (pos[0] + len(text), pos[1]+1)
		self.drawrect(bottomleft,topright)
		self.drawtext(text,pos)

	def draw(self,draw_axis=False):
		if draw_axis:
			xaxis = [str(x % 10) for x in range(len(self.canvas[0]))]
		else:
			xaxis = []
		xaxis.insert(0,' ')
		output = []
		output.insert(0,''.join(xaxis))
		for i,line in enumerate(self.canvas):
			if draw_axis:
				line.insert(0,str(i%10))
			output.insert(0,''.join(line))

		for line in output:
			print(line)

	def drawline(self,style,start,end):
		angle = math.atan2(float(end[1]-start[1]),float(end[0]-start[0]))
		pos = start
		while True:
			pos = (pos[0]+math.cos(angle),pos[1]+math.sin(angle))
			if abs(pos[0]-end[0]) < 1 and abs(pos[1]-end[1]) < 1:
				break
			self.__insert(math.floor(pos[1]),math.floor(pos[0]),style)
