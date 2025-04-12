class Element:
    def __init__(self, **kwargs):
        self.tag = None # defined in child classes
        self.attributes = {}
        self.content = None # defined in child classes where relevant
        self.styles = {}
        self.styles['fill'] = kwargs.get('fill', None)
        self.styles['stroke'] = kwargs.get('stroke', None)
        self.styles['stroke-width'] = kwargs.get('strokewidth', None)
        self.styles['opacity'] = kwargs.get('opacity', None)
        self.transformations = []
        
    def translate(self, dx, dy):
        self.transformations.append(f"translate({dx},{dy})")
        return self
    
    def rotate(self, angle, cx=None, cy=None):
        if cx is not None and cy is not None:
            self.transformations.append(f"rotate({angle} {cx} {cy})")
        else:
            self.transformations.append(f"rotate({angle})")
        return self
    
    def scale(self, sx, sy=None):
        if sy is not None:
            self.transformations.append(f"scale({sx} {sy})")
        else:
            self.transformations.append(f"scale({sx})")
        return self
    
    def skew(self, x=None, y=None):
        if x is not None:
            self.transformations.append(f"skewX({x})")
        if y is not None:
            self.transformations.append(f"skewY({y})")
        return self

    def to_svg(self):
        svg_string = self.add_open_tag_svg()
        svg_string += self.add_content_svg()
        svg_string += f"</{self.tag}>"
        return svg_string

    def add_open_tag_svg(self):
        open_tag_svg = f"<{self.tag}{self.add_attribute_svg()}{self.add_transform_svg()}{self.add_style_svg()}>"
        return open_tag_svg

    def add_attribute_svg(self):
        attribute_svg = ""
        for attribute,value in self.attributes.items():
            attribute_svg += f' {attribute}="{value}"'
        return attribute_svg
    
    def add_style_svg(self):
        styling_svg = ""
        inline_styles = []
        for style_attribute, value in self.styles.items():
            if value is not None:
                inline_styles.append(f"{style_attribute}: {value};")
        if inline_styles:
            styling_svg = f' style="{" ".join(inline_styles)}"'
        return styling_svg

    def add_transform_svg(self):
        if self.transformations:
            return f''' transform="{" ".join(self.transformations)}"'''
        return ""

    def add_content_svg(self):
        return self.content