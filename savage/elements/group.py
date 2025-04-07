from .element import Element

class Group(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.children = []
        
    def add(self):
        pass
        
    def to_svg(self):
        return super().to_svg()