from savage import Element

# for testing to_svg()
class DummyElement(Element):
    def to_svg(self):
        return f"<dummy {self.generate_style_svg()}/>"


def test_add_styling_with_all_attributes():
    test_element = DummyElement(fill="red", stroke="blue", strokewidth=2)
    svg = test_element.generate_style_svg()
    assert 'fill="red"' in svg
    assert 'stroke="blue"' in svg
    assert 'stroke-width="2"' in svg

def test_add_styling_with_some_attributes():
    test_element = DummyElement(fill="green")
    svg = test_element.generate_style_svg()
    assert 'fill="green"' in svg
    assert 'stroke=' not in svg
    assert 'stroke-width=' not in svg

def test_add_styling_with_no_attributes():
    test_element = DummyElement()
    svg = test_element.generate_style_svg()
    assert svg.strip() == ""
