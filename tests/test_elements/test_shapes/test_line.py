from savage import Line

def test_line_basic_attributes():
    line = Line(x1=0, y1=0, x2=100, y2=100)
    svg = line.to_svg()
    assert 'x1="0"' in svg
    assert 'y1="0"' in svg
    assert 'x2="100"' in svg
    assert 'y2="100"' in svg

def test_line_to_svg_format():
    line = Line(x1=1, y1=2, x2=3, y2=4)
    svg = line.to_svg().strip()
    assert svg.startswith("<line")
    assert svg.endswith("/>")
