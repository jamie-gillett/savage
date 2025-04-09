from elements import Element

class Graphic:
    def __init__(self, width=None, height=None, background=None):
        self.width = width
        self.height = height
        self.background = background
        self.elements: list[Element] = []
        
    def add(self, element:Element):
        self.elements.append(element)

    def to_svg(self):
        svg_string = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n"""
        width_svg = f' width="{self.width}"' if self.width is not None else ""
        height_svg = f' height="{self.height}"' if self.height is not None else ""
        svg_string += f"""<svg xmlns="http://www.w3.org/2000/svg"{width_svg}{height_svg}>\n"""
        if self.background:
            svg_string += f'  <rect width="100%" height="100%" fill="{self.background}" />\n'
        for element in self.elements:
            svg_string += "  " + element.to_svg() + "\n"
        svg_string += """</svg>"""
        return svg_string
    
    def save(self, filepath):
        svg_string = self.to_svg()
        with open(filepath, 'w') as output:
            output.write(svg_string)