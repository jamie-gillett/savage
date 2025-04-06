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


class Rect(Element):
    def __init__(self, width, height, x, y, rx=None, ry=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        
    def to_svg(self):
        svg_string = f"""<rect width="{self.width}" height="{self.height}" x="{self.x}" y="{self.y}" """
        if self.rx:
            svg_string += f"""rx="{self.rx}" """
        if self.ry:
            svg_string += f"""ry="{self.ry}" """
        svg_string += "/>\n"
        return svg_string


class Circle(Element):
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
        
    def to_svg(self):
        svg_string = f"""<circle r="{self.r}" cx="{self.cx}" cy="{self.cy}" />\n"""
        return svg_string


class Ellipse(Element):
    def __init__(self, cx, cy, rx, ry):
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
    
    def to_svg(self):
        svg_string = f"""<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" />\n"""
        return svg_string


class Line(Element):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def to_svg(self):
        pass


class Text(Element):
    def __init__(self):
        pass

    def to_svg(self):
        pass

