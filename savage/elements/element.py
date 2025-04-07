class Element:
    def __init__(self, **kwargs):
        self.fill = kwargs['fill'] if 'fill' in kwargs else None
        self.stroke = kwargs['stroke'] if 'stroke' in kwargs else None
        self.strokewidth = kwargs['strokewidth'] if 'strokewidth' in kwargs else None
        
    def to_svg(self):
        pass

    def add_styling(self):
        styling = ""
        if self.fill:
            styling += f"""fill="{self.fill}" """
        if self.stroke:
            styling += f"""stroke="{self.stroke}" """
        if self.strokewidth:
            styling += f"""stroke-width="{self.strokewidth}" """
        return styling