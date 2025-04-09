# Savage Examples

This page provides a few examples showcasing the capabilities of the **savage** Python package for programmatic SVG generation.

Each example includes a short description, the code used to generate the SVG, and the resulting output.

---

## Example 1: Basic Circle

A simple red circle with a black stroke.

```Python
from savage import Circle, Graphic

g = Graphic(width=100, height=100)
c = Circle(cx=50, cy=50, r=40, fill="red", stroke="black", strokewidth=2)
g.add(c)
g.save("output.svg")
```

![Circle Example](example_1/output.svg)

<details>
	<summary>svg output</summary>
	
	```xml
	<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
		<circle cx="50" cy="50" r="40" fill="red" stroke="black" stroke-width="2" />
	</svg>
	```
</details>

---

## Example 2: Transformed Rectangle

A rectangle that has been rotated and translated using transformation chaining.

```Python
from savage import Rect, Graphic

g = Graphic(width=100, height=100)
r = Rect(x=10, y=10, width=80, height=40, rx=5, ry=5, fill="blue", stroke="black").rotate(10).translate(10,10)
g.add(r)
g.save("output.svg")
```

![Transformed Rectangle](example_2/output.svg)

<details>
	<summary>svg output</summary>
	
	```xml
	<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
		<rect width="80" height="40" x="10" y="10" rx="5" ry="5" transform="rotate(10) translate(10,10)" fill="blue" stroke="black" />
	</svg>
	```
</details>

---

## Example 3: Polygon and Polyline

A polygon and a polyline created from a list of points.

```Python
from savage import Polygon, Polyline, Graphic

g = Graphic(width=70, height=90)
p = Polygon(points=[10,10, 60,10, 35,50], fill="lime", stroke="green")
l = Polyline(points=[10,60, 30,80, 50,60], fill="transparent", stroke="black", strokewidth=2)
g.add(p)
g.add(l)
g.save("output.svg")
```

![Polygon and Polyline](example_3/output.svg)

<details>
	<summary>svg output</summary>
	
	```xml
	<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<svg xmlns="http://www.w3.org/2000/svg" width="70" height="90">
		<polygon points="10,10 60,10 35,50" fill="lime" stroke="green" />
		<polyline points="10,60 30,80 50,60" fill="transparent" stroke="black" stroke-width="2" />
	</svg>
	```
</details>

---

## Example 4: Styled Text

Text with custom font, color, and alignment.

```Python
from savage import Text, Graphic

g = Graphic(width=100, height=20)
t = Text(x=50, y=10, content="Hello, SVG!", fill="red", fontfamily="Courier", anchor="middle", baseline="middle")
g.add(t)
g.save("output.svg")
```

![Styled Text](example_4/output.svg)

<details>
	<summary>svg output</summary>
	
	```xml
	<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<svg xmlns="http://www.w3.org/2000/svg" width="100" height="20">
		<text x="50" y="10" fill="red" text-anchor="middle" dominant-baseline="middle">Hello, SVG!</text>
	</svg>
	```
</details>

---

## Example 5: Combined Graphic

Multiple shapes and text combined into one graphic.

```Python
from savage import Circle, Rect, Text, Graphic

g = Graphic(width=200, height=200)

g.add(Circle(cx=30, cy=30, r=20, fill="yellow"))
g.add(Rect(x=60, y=20, width=40, height=20, fill="skyblue"))
g.add(Text(x=10, y=80, content="Shapes!", fill="blue", fontfamily="Verdana"))

g.save("output.svg")
```

![Combined Graphic](example_5/output.svg)

<details>
	<summary>svg output</summary>
	
	```xml
	<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
		<circle cx="30" cy="30" r="20" fill="yellow" />
		<rect width="40" height="20" x="60" y="20" fill="skyblue" />
		<text x="10" y="80" fill="blue">Shapes!</text>
	</svg>
	```
</details>

---

These are just a few examples — the `savage` library is designed to be flexible, composable, and lightweight for use in creative and scientific projects alike.
