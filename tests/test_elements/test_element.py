from savage import Element

# DummyElement for style and attribute testing
class DummyElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# DummyTagElement to test base class to_svg() method
class DummyTagElement(Element):
    def __init__(self):
        super().__init__(fill="black")
        self.tag = "dummy"
        self.attributes = {"x": 10}
        self.content = "Hello"

def test_add_style_svg_all_attributes():
    dummy_element = DummyElement(fill="red", stroke="blue", strokewidth=2)
    result = dummy_element.add_style_svg()
    assert 'fill="red"' in result
    assert 'stroke="blue"' in result
    assert 'stroke-width="2"' in result

def test_add_style_svg_some_attributes():
    dummy_element = DummyElement(fill="green")
    result = dummy_element.add_style_svg()
    assert 'fill="green"' in result
    assert 'stroke=' not in result
    assert 'stroke-width=' not in result

def test_add_style_svg_no_attributes():
    dummy_element = DummyElement()
    result = dummy_element.add_style_svg()
    assert result.strip() == ""

def test_add_attribute_svg():
    dummy_element = DummyElement()
    dummy_element.attributes = {"cx": 50, "cy": 100}
    result = dummy_element.add_attribute_svg()
    assert 'cx="50"' in result
    assert 'cy="100"' in result

def test_add_attribute_svg_empty():
    dummy_element = DummyElement()
    result = dummy_element.add_attribute_svg()
    assert result.strip() == ""

def test_element_to_svg_base_method():
    dummy_element = DummyTagElement()
    result = dummy_element.to_svg()

    assert result.startswith("<dummy ")
    assert 'x="10"' in result
    assert 'fill="black"' in result
    assert "Hello" in result
    assert result.endswith("</dummy>")
