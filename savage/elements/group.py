from .element import Element

class Group(Element):
    def __init__(self, children=None, **kwargs):
        super().__init__(**kwargs)
        self.children: list[Element] = children if children is not None else []
        
    def add(self, element:Element):
        self.children.append(element)
        
    def to_svg(self):
        svg_string = f"""<g {self.add_styling()}>\n"""
        for element in self.children:
            svg_string += "\t" + element.to_svg()
        svg_string += "</g>"
        return svg_string