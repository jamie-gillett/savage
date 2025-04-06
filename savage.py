class Element:
    def to_svg(self):
        pass

class Graphic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.elements: list[Element] = []
        
    def add(self, element:Element):
        self.elements.append(element)
    
    def to_svg(self):
        svg_string = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n"""
        svg_string += f"""<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}">\n"""
        for element in self.elements:
            svg_string += "\t" + element.to_svg()
        svg_string += """</svg>"""
        return svg_string
    
    def save(self, filepath):
        svg_string = self.to_svg()
        with open(filepath, 'w') as output:
            output.write(svg_string)

class Circle(Element):
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
        
    def to_svg(self):
        svg_string = f"""<circle r="{self.r}" cx="{self.cx}" cy="{self.cy}" />\n"""
        return svg_string

class Rect(Element):
    def __init__(self, width, height, x, y, rx=0, ry=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        
    def to_svg(self):
        svg_string = f"""<rect width="{self.width}" height="{self.height}" x="{self.x}" y="{self.y}" rx="{self.rx}" ry="{self.ry}" />\n"""
        return svg_string

class Line(Element):
    pass

class Text(Element):
    pass

