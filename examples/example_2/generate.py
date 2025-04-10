from savage import Graphic, Circle, Text

g = Graphic(width=340, height=120, background="white")
g.add( Circle(cx=60, cy=60, r=50, fill="cornsilk") )
g.add( Text(x=60, y=60, content="fill") )
g.add( Circle(cx=170, cy=60, r=50, stroke="red") )
g.add( Text(x=170, y=60, content="stroke") )
g.add( Circle(cx=280, cy=60, r=50, strokewidth=4) )
g.add( Text(x=280, y=60, content="stroke-width") )

g.save("output.svg")