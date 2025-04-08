from savage import Text

def test_text_includes_position_attributes():
    text = Text(x=10, y=20, content="Hello SVG")
    svg = text.to_svg()
    
    assert 'x="10"' in svg
    assert 'y="20"' in svg

def test_text_includes_content_between_tags():
    text = Text(x=0, y=0, content="Sample Text")
    svg = text.to_svg()
    
    assert ">Sample Text<" in svg

def test_text_applies_styling_correctly():
    text = Text(x=0, y=0, content="Styled", fill="red", stroke="blue", strokewidth=2)
    svg = text.to_svg()
    
    assert 'fill="red"' in svg
    assert 'stroke="blue"' in svg
    assert 'stroke-width="2"' in svg

def test_text_svg_tag_structure():
    text = Text(x=5, y=5, content="Format")
    svg = text.to_svg().strip()
    
    assert svg.startswith("<text")
    assert svg.endswith("</text>")
