from savage import Polygon, Polyline, Graphic

g = Graphic(width=70, height=90)
p = Polygon(points=[10,10, 60,10, 35,50], fill="lime", stroke="green")
l = Polyline(points=[10,60, 30,80, 50,60], fill="transparent", stroke="black", strokewidth=2)
g.add(p)
g.add(l)
g.save("output.svg")