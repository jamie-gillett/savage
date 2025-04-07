from ..element import Element

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