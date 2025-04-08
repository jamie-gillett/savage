from savage import Shape

# A simple concrete subclass for testing purposes
class DummyShape(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tag = "dummy"
        self.attributes["x"] = 10
        self.attributes["y"] = 20

def test_shape_generates_self_closing_tag():
    shape = DummyShape()
    svg = shape.to_svg()
    
    assert svg.startswith("<dummy")
    assert svg.endswith(" />")

def test_shape_includes_attributes():
    shape = DummyShape()
    svg = shape.to_svg()

    assert 'x="10"' in svg
    assert 'y="20"' in svg

def test_shape_applies_styles_correctly():
    shape = DummyShape(fill="red", stroke="black", strokewidth=1)
    svg = shape.to_svg()
    
    assert 'fill="red"' in svg
    assert 'stroke="black"' in svg
    assert 'stroke-width="1"' in svg
