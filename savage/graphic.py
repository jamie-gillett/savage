from elements import Element, Shape

class Graphic:
    def __init__(self, width=None, height=None, background=None, **kwargs):
        self.width = width
        self.height = height
        self.background = background
        self.elements: list[Element] = []
        self.tags_used = []
        self.default_styles = {}
        self.default_styles['fill'] = kwargs.get('fill', '#E6E6FA')
        self.default_styles['stroke'] = kwargs.get('stroke', '#A39EB2')
        self.default_styles['stroke-width'] = kwargs.get('strokewidth', 2)
        
    def add(self, element:Element):
        self.elements.append(element)
        if isinstance(element, Shape) and element.tag not in self.tags_used:
            self.tags_used.append(element.tag)
            self.tags_used.sort()

    def to_svg(self):
        svg_string = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n"""
        width_svg = f' width="{self.width}"' if self.width is not None else ""
        height_svg = f' height="{self.height}"' if self.height is not None else ""
        svg_string += f"""<svg xmlns="http://www.w3.org/2000/svg"{width_svg}{height_svg}>\n"""
        if self.tags_used:
            svg_string += "  <style>\n"
            svg_string += f'''    {" ".join(self.tags_used)} {{\n'''
            svg_string += f'''      fill: {self.default_styles['fill']}'''
            svg_string += f'''      stroke: {self.default_styles['stroke']}'''
            svg_string += f'''      stroke-width: {self.default_styles['stroke-width']}'''
            svg_string += '    }'
            svg_string += "  </style>\n"
        if self.background:
            svg_string += f'  <rect width="100%" height="100%" style="fill: {self.background};" />\n'
        for element in self.elements:
            svg_string += "  " + element.to_svg() + "\n"
        svg_string += """</svg>"""
        return svg_string
    
    def save(self, filepath):
        svg_string = self.to_svg()
        with open(filepath, 'w') as output:
            output.write(svg_string)