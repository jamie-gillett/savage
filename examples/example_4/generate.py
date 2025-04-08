from savage import Text, Graphic

g = Graphic(width=100, height=20)
t = Text(x=50, y=10, content="Hello, SVG!", fill="red", fontfamily="Courier", anchor="middle", baseline="middle")
g.add(t)
g.save("output.svg")