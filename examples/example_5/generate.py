from savage import Circle, Rect, Text, Graphic

g = Graphic(width=200, height=200)

g.add(Circle(cx=30, cy=30, r=20, fill="yellow"))
g.add(Rect(x=60, y=20, width=40, height=20, fill="skyblue"))
g.add(Text(x=10, y=80, content="Shapes!", fill="blue", fontfamily="Verdana"))

g.save("output.svg")