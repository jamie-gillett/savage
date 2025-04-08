from savage import Line

def test_line_basic_attributes():
    line = Line(x1=0, y1=0, x2=100, y2=100)
    svg = line.to_svg()
    assert 'x1="0"' in svg
    assert 'y1="0"' in svg
    assert 'x2="100"' in svg
    assert 'y2="100"' in svg

def test_line_default_stroke():
    line = Line(x1=0, y1=0, x2=50, y2=50)
    svg = line.to_svg()
    assert 'stroke="black"' in svg  # Default stroke is set in constructor

def test_line_custom_stroke_and_styling():
    line = Line(x1=10, y1=20, x2=30, y2=40, stroke="blue", strokewidth="3")
    svg = line.to_svg()
    assert 'stroke="blue"' in svg
    assert 'stroke-width="3"' in svg

def test_line_to_svg_format():
    line = Line(x1=1, y1=2, x2=3, y2=4)
    svg = line.to_svg().strip()
    assert svg.startswith("<line")
    assert svg.endswith("/>")
