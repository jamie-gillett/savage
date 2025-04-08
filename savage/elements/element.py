class Element:
    def __init__(self, **kwargs):
        self.tag = None # defined in child classes
        self.attributes = {}
        self.content = None # defined in child classes where relevant
        self.styles = {}
        self.styles['fill'] = kwargs.get('fill', None)
        self.styles['stroke'] = kwargs.get('stroke', None)
        self.styles['stroke-width'] = kwargs.get('strokewidth', None)

    def to_svg(self):
        svg_string = self.add_open_tag_svg()
        svg_string += self.add_content_svg()
        svg_string += f"</{self.tag}>"
        return svg_string

    def add_open_tag_svg(self):
        open_tag_svg = f"<{self.tag}{self.add_attribute_svg()}{self.add_style_svg()}>"
        return open_tag_svg

    def add_attribute_svg(self):
        attribute_svg = ""
        for attribute,value in self.attributes.items():
            attribute_svg += f' {attribute}="{value}"'
        return attribute_svg

    def add_content_svg(self):
        return self.content
    
    def add_style_svg(self):
        styling_svg = ""
        for style_attribute, value in self.styles.items():
            if value:
                styling_svg += f' {style_attribute}="{value}"'
        return styling_svg