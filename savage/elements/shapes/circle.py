from .shape import Shape

class Circle(Shape):
    def __init__(self, cx, cy, r, **kwargs):
        super().__init__(**kwargs)
        self.tag = "circle"
        self.cx = cx
        self.cy = cy
        self.r = r
        
    def to_svg(self):
        svg_string = f"""<circle r="{self.r}" cx="{self.cx}" cy="{self.cy}" {self.generate_style_svg()}/>\n"""
        return svg_string