class Element:
    def __init__(self, **kwargs):
        self.fill = kwargs['fill'] if 'fill' in kwargs else None
        self.stroke = kwargs['stroke'] if 'stroke' in kwargs else None
        self.strokewidth = kwargs['strokewidth'] if 'strokewidth' in kwargs else None
        
    def to_svg(self):
        pass

    def add_styling(self):
        styling = ""
        if self.fill:
            styling += f"""fill="{self.fill}" """
        if self.stroke:
            styling += f"""stroke="{self.stroke}" """
        if self.strokewidth:
            styling += f"""stroke-width="{self.strokewidth}" """
        return styling



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
    def __init__(self, width, height, x, y, rx=None, ry=None, **kwargs):
        super().__init__(**kwargs)
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
        svg_string += self.add_styling()
        svg_string += "/>\n"
        return svg_string



class Circle(Element):
    def __init__(self, cx, cy, r, **kwargs):
        super().__init__(**kwargs)
        self.cx = cx
        self.cy = cy
        self.r = r
        
    def to_svg(self):
        svg_string = f"""<circle r="{self.r}" cx="{self.cx}" cy="{self.cy}" {self.add_styling()}/>\n"""
        return svg_string



class Ellipse(Element):
    def __init__(self, cx, cy, rx, ry, **kwargs):
        super().__init__(**kwargs)
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
    
    def to_svg(self):
        svg_string = f"""<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" {self.add_styling()}/>\n"""
        return svg_string



class Line(Element):
    def __init__(self, x1, y1, x2, y2, **kwargs):
        super().__init__(**kwargs)
        if not self.stroke:
            self.stroke = "black"
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def to_svg(self):
        svg_string = f"""<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" {self.add_styling()}/>\n"""
        return svg_string
    


class Text(Element):
    def __init__(self, x, y, content, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.content = content

    def to_svg(self):
        svg_string = f"""<text x="{self.x}" y="{self.y}"{self.add_styling()}>{self.content}</text>\n"""
        return svg_string
    
    def add_styling(self):
        svg_string = ""
        if self.fill:
            svg_string += f''' fill="{self.fill}"'''
        if self.stroke:
            svg_string += f''' stroke="{self.stroke}"'''
        if self.strokewidth:
            svg_string += f''' stroke-wdith="{self.strokewidth}"'''
        return svg_string