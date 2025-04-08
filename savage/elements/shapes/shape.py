from ..element import Element

class Shape(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def to_svg(self):
        svg_string = self.add_open_tag_svg()
        svg_string = svg_string.replace(">"," />")
        return svg_string