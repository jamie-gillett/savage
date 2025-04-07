from ..element import Element

class Circle(Element):
    def __init__(self, cx, cy, r, **kwargs):
        super().__init__(**kwargs)
        self.cx = cx
        self.cy = cy
        self.r = r
        
    def to_svg(self):
        svg_string = f"""<circle r="{self.r}" cx="{self.cx}" cy="{self.cy}" {self.add_styling()}/>\n"""
        return svg_string