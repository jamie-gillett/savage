from .element import Element

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