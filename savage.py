class Graphic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.elements: list[Element] = []
    
    def to_svg(self):
        svg_string = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n"""
        svg_string += f"""<svg xmlns="http://www.w3.org/2000/svg" width={self.width} height={self.height}>\n"""
        for element in self.elements:
            svg_string += "\t" + element.to_svg() + "\n"
        svg_string += """</svg>"""
        return svg_string
    
    def save(self, filepath):
        svg_string = self.to_svg()
        with open(filepath) as output:
            output.write(svg_string)

class Element:
    def to_svg(self):
        pass
    
    
