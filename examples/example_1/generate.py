from savage import Graphic, Circle, Rect, Ellipse, Line, Polygon, Polyline, Text

g = Graphic(width=670, height=120)
g.add(Circle(cx=60,cy=60,r=50))
g.add(Text(x=60, y=60, content="circle"))
g.add(Rect(width=100, height=80, x=120, y=20, rx=10, ry=10))
g.add(Text(x=170, y=60, content="rect"))
g.add(Ellipse(cx=280, cy=60, rx=50, ry=40))
g.add(Text(x=280, y=60, content="ellipse"))
g.add(Line(x1=340, y1=110, x2=440, y2=10))
g.add(Text(x=390, y=60, content="line"))
g.add(Polyline(points=[450,110, 450,10, 550,10]))
g.add(Text(x=500, y=60, content="polyline"))
g.add(Polygon(points=[560,110, 660,110, 660,10]))
g.add(Text(x=610, y=60, content="polygon"))

g.save("output.svg")