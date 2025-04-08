from .element import Element

class Text(Element):
    def __init__(self, x, y, content, **kwargs):
        super().__init__(**kwargs)
        self.tag = "text"
        self.attributes['x'] = x
        self.attributes['y'] = y
        self.content = content