# Savage

Savage is a lightweight and modular SVG generator written in Python. Designed with an object-oriented structure, it lets you build entire SVG documents programmatically — from simple shapes and text to complex, nested groups.

At its core is the `Graphic` class, which represents a complete SVG document. Combined with a growing library of SVG elements like `Circle`, `Ellipse`, `Line`, `Polygon`, `Polyline`, `Rect`, `Text` and `Group`, Savage makes it easy (not really) to construct and style SVG graphics dynamically.

## Features

- ⚙️ Build full SVG documents with the `Graphic` class
- 🔵 Create shapes: `Circle`, `Ellipse`, `Line`, `Polygon`, `Polyline`, `Rect`
- 📝 Add text labels with styling via the `Text` class
- 🧩 Group elements together using `Group` for hierarchical layouts
- 🎨 Set attributes like position, fill, stroke, font size, and more
- 🧱 Clean, extensible architecture for adding new SVG element types
- 🧪 Built-in support for testing and development via `pytest`


## Installation

To install Savage for use in other projects, use:
``` bash
pip install savage-generator
```


To install Savage in editable mode (for development), follow these steps:

### Clone the repository  
``` bash
git clone https://github.com/jamie-gillett/savage.git
cd savage
```

### Install the package in editable mode  
``` bash
pip install -e .
```

### Installation with test setup
``` bash
pip install -e .[dev]
```

## Usage

Savage is built around combining individual SVG elements into a full document. You can create shapes and text, organize them into groups, and output valid SVG markup using the `Graphic` class.

### Create and render a simple SVG

``` Python
from savage import Graphic, Circle, Rect, Text, Group

# Create a red rectangle and a blue circle
rect = Rect(x=10, y=10, width=200, height=100, fill="red")
circle = Circle(cx=110, cy=60, r=40, fill="blue")

# Add a label
label = Text(x=60, y=65, content="Hello SVG!", fill="white", font_size="18")

# Group them together
group = Group(content=[rect, circle, label])

# Create the SVG document and add the group
doc = Graphic(width=300, height=150)
doc.add(group)

# Print the full SVG
print(doc.to_svg())
```

This will output SVG markup that you can save to a file or embed in a webpage.

### Save to a file

``` Python
# Save the SVG to a file
doc.save("output.svg")
```

## Running Tests

To run the tests, simply run:

### Run tests using pytest  
``` bash
pytest
```
