class Element:
    def __init__(self, **kwargs):
        self.tag = None # defined in child classes
        self.fill = kwargs.get('fill', None)
        self.stroke = kwargs.get('stroke', None)
        self.strokewidth = kwargs.get('strokewidth', None)
        
    def to_svg(self):
        svg_string = self.generate_open_tag_svg()
        svg_string += self.generate_content_svg()
        svg_string += self.generate_end_tag_svg()
        return svg_string
    
    def generate_open_tag_svg(self):
        open_tag_svg = ""
        return open_tag_svg
    
    def generate_content_svg(self):
        pass
    
    def generate_end_tag_svg(self):
        pass

    def generate_style_svg(self):
        styling = ""
        if self.fill:
            styling += f"""fill="{self.fill}" """
        if self.stroke:
            styling += f"""stroke="{self.stroke}" """
        if self.strokewidth:
            styling += f"""stroke-width="{self.strokewidth}" """
        return styling