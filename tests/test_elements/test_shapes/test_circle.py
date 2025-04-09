from savage import Circle

def test_circle_basic_attributes():
    c = Circle(cx=50, cy=75, r=25)
    svg = c.to_svg()
    assert '<circle' in svg
    assert 'cx="50"' in svg
    assert 'cy="75"' in svg
    assert 'r="25"' in svg
   
def test_circle_output_format():
    c = Circle(cx=0, cy=0, r=10)
    svg = c.to_svg().strip()
    assert svg.startswith("<circle")
    assert svg.endswith("/>")