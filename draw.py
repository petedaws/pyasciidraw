import math



def drawdot(canvas,pos):
    canvas[pos[1]][pos[0]] = '+'


def drawbox(canvas,center,size):

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

def create_canvas(x,y):
    output = []
    for a in range(y):
        line = []
        for b in range(x):
            line.append(' ')
        output.append(line)
    return output

def draw(canvas):
    xaxis = [str(x % 10) for x in range(len(canvas[0]))]
    print(''.join(xaxis))
    for i,line in enumerate(canvas):
        print(i%10,''.join(line))

def drawline(canvas,style,x1,y1,x2,y2):
    angle = math.atan2(float(y2-y1),float(x2-x1))
    pos = (x1,y1)
    while True:
        pos = (pos[0]+math.cos(angle),pos[1]+math.sin(angle))
        if abs(pos[0]-x2) < 1 and abs(pos[1]-y2) < 1:
            break
        canvas[math.floor(pos[1])][math.floor(pos[0])] = style
        

canvas = create_canvas(100,20)
drawbox(canvas,(5,5),3)
drawbox(canvas,(10,10),1)
drawbox(canvas,(15,15),2)
drawline(canvas,'+',7,7,2,2)
draw(canvas)

    
