from savage.elements.text import Text

def test_text_basic_content_and_position():
    text = Text(x=10, y=20, content="Hello SVG")
    svg = text.to_svg()
    assert 'x="10"' in svg
    assert 'y="20"' in svg
    assert ">Hello SVG<" in svg

def test_text_with_styling():
    text = Text(x=0, y=0, content="Styled", fill="red", stroke="blue", strokewidth="2")
    svg = text.to_svg()
    assert 'fill="red"' in svg
    assert 'stroke="blue"' in svg
    assert 'stroke-width="2"' in svg

def test_text_svg_format():
    text = Text(x=5, y=5, content="Test")
    svg = text.to_svg().strip()
    assert svg.startswith("<text")
    assert svg.endswith("</text>")
