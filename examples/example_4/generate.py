from random import randint, random
from savage import Graphic, Rect

cols = 8
rows = 8

target = (randint(3,cols-3), randint(3,rows-3))

size = 64
margin = 8

g = Graphic(width=margin+cols*(size+margin), height=margin+rows*(size+margin), background="white")

for r_i in range(rows):
    for c_i in range(cols):
        if c_i in [target[0]-1, target[0], target[0]+1] and r_i in [target[1]-1, target[1], target[1]+1]:
            continue
        v = randint(25,50)
        g.add( Rect(width=size, height=size, x=margin+c_i*(size+margin), y=margin+r_i*(size+margin), fill=f"RGB({v},{v},{v})", stroke="none") )
        
for r_i in range(-1,2):
    for c_i in range(-1,2):
        if r_i == 0 and c_i == 0:
            continue
        col = target[0] + c_i
        row = target[1] + r_i
        posX = margin+col*(size+margin)
        posY = margin+row*(margin+size)
        v = randint(25,50)
        hue = randint(10,20)
        border_rect = Rect(width=size, height=size, x=posX, y=posY, fill=f"RGB({v+hue},{v},{v})", stroke="none")
        border_rect.rotate((random()-0.5)*5, cx=posX+size/2, cy=posY+size/2)
        g.add(border_rect)
        
for i in range(size//2+2*margin):
    tgtX = margin+target[0]*(size+margin)+size//2
    tgtY = margin+target[1]*(size+margin)+size//2
    r = Rect(width=(i+1)*2, height=(i+1)*2, x=tgtX-i-1, y=tgtY-i-1, fill="none", stroke=f"RGB(220,20,60)", strokewidth=random()*2+0.1, opacity=f"{randint(50,75)}%")
    angle = 24 * (i/(size//2)) * (random()-0.5)
    r.rotate(angle=angle, cx=tgtX, cy=tgtY)
    g.add(r)

g.save("output.svg")