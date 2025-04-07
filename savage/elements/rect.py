from ..element import Element

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