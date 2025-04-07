class Element:
    def __init__(self, **kwargs):
        self.tag = None # defined in child classes
        self.attributes = {}
        self.content = None # defined in child classes
        self.fill = kwargs.get('fill', None)
        self.stroke = kwargs.get('stroke', None)
        self.strokewidth = kwargs.get('strokewidth', None)

    def to_svg(self):
        svg_string = self.generate_open_tag_svg()
        svg_string += self.generate_content_svg()
        svg_string += f"</{self.tag}>"
        return svg_string

    def generate_open_tag_svg(self):
        open_tag_svg = f"<{self.tag}{self.generate_attribute_svg()}{self.generate_style_svg()}>"
        return open_tag_svg

    def generate_attribute_svg(self):
        attribute_svg = ""
        for attribute,value in self.attributes.items():
            attribute_svg += f' {attribute}="{value}"'
        return attribute_svg

    def generate_content_svg(self):
        return self.content
    
    def generate_style_svg(self):
        styling_svg = ""
        if self.fill:
            styling_svg += f''' fill="{self.fill}"'''
        if self.stroke:
            styling_svg += f''' stroke="{self.stroke}"'''
        if self.strokewidth:
            styling_svg += f''' stroke-width="{self.strokewidth}"'''
        return styling_svg