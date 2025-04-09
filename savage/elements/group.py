from .element import Element

class Group(Element):
    def __init__(self, children=None, **kwargs):
        super().__init__(**kwargs)
        self.tag = "g"
        self.content: list[Element] = children if children is not None else []
        
    def add(self, element:Element):
        self.content.append(element)
        
    def add_open_tag_svg(self):
        return super().add_open_tag_svg() +"\n"
    
    def add_content_svg(self):
        content_svg = ""
        for element in self.content:
            content_svg += "  " + element.to_svg() + "\n"
        return content_svg