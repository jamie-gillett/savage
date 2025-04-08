from savage import Element

# DummyElement for testing
class DummyElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tag = "dummy"
        self.content = "Content"

    def to_svg(self):
        return super().to_svg()


def test_styles_all_set():
    el = DummyElement(fill="red", stroke="blue", strokewidth=2)
    svg = el.to_svg()
    assert 'fill="red"' in svg
    assert 'stroke="blue"' in svg
    assert 'stroke-width="2"' in svg

def test_styles_partial():
    el = DummyElement(fill="green")
    svg = el.to_svg()
    assert 'fill="green"' in svg
    assert 'stroke=' not in svg
    assert 'stroke-width=' not in svg

def test_no_styles():
    el = DummyElement()
    svg = el.to_svg()
    assert 'fill=' not in svg
    assert 'stroke=' not in svg

def test_basic_output_structure():
    el = DummyElement()
    svg = el.to_svg().strip()
    assert svg.startswith("<dummy")
    assert svg.endswith("</dummy>")
    assert ">Content<" in svg

def test_add_attribute_svg():
    el = DummyElement()
    el.attributes["x"] = 10
    el.attributes["y"] = 20
    svg = el.to_svg()
    assert 'x="10"' in svg
    assert 'y="20"' in svg

def test_transform_translate():
    el = DummyElement().translate(10, 20)
    svg = el.to_svg()
    assert 'transform="translate(10,20)"' in svg

def test_transform_rotate_no_origin():
    el = DummyElement().rotate(45)
    svg = el.to_svg()
    assert 'transform="rotate(45)"' in svg

def test_transform_rotate_with_origin():
    el = DummyElement().rotate(30, cx=5, cy=5)
    svg = el.to_svg()
    assert 'transform="rotate(30 5 5)"' in svg

def test_transform_scale_one_arg():
    el = DummyElement().scale(2)
    svg = el.to_svg()
    assert 'transform="scale(2)"' in svg

def test_transform_scale_two_args():
    el = DummyElement().scale(2, 3)
    svg = el.to_svg()
    assert 'transform="scale(2 3)"' in svg

def test_transform_skew_x():
    el = DummyElement().skew(x=45)
    svg = el.to_svg()
    assert 'transform="skewX(45)"' in svg

def test_transform_skew_y():
    el = DummyElement().skew(y=30)
    svg = el.to_svg()
    assert 'transform="skewY(30)"' in svg

def test_transform_combined_order():
    el = DummyElement().translate(10, 10).rotate(45).scale(2)
    svg = el.to_svg()
    assert 'transform="translate(10,10) rotate(45) scale(2)"' in svg
