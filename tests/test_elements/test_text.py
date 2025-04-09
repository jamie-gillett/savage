from savage import Text

def test_text_basic():
    t = Text(x=100, y=200, content="Hello SVG")
    svg = t.to_svg()
    assert '<text' in svg
    assert 'x="100"' in svg
    assert 'y="200"' in svg
    assert 'Hello SVG' in svg
    assert svg.endswith("</text>")

def test_text_with_font_and_alignment():
    t = Text(x=50, y=50, content="Aligned Text", font="Verdana", anchor="middle", baseline="middle")
    svg = t.to_svg()
    assert 'font-family: Verdana;' in svg
    assert 'text-anchor: middle;' in svg
    assert 'dominant-baseline: middle;' in svg

def test_text_with_transformations():
    t = Text(x=0, y=0, content="Rotated").rotate(45)
    svg = t.to_svg()
    assert 'transform="rotate(45)"' in svg