from savage import Rect, Graphic

g = Graphic(width=100, height=100)
r = Rect(x=10, y=10, width=80, height=40, rx=5, ry=5, fill="blue", stroke="black").rotate(10).translate(10,10)
g.add(r)
g.save("output.svg")