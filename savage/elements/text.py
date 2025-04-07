from .element import Element

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