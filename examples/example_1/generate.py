from savage import Circle, Graphic

g = Graphic(width=100, height=100)
c = Circle(cx=50, cy=50, r=40, fill="red", stroke="black", strokewidth=2)
g.add(c)
g.save("output.svg")