from savage import Ellipse

def test_ellipse_basic_attributes():
    ellipse = Ellipse(cx=50, cy=60, rx=30, ry=20)
    svg = ellipse.to_svg()
    assert 'cx="50"' in svg
    assert 'cy="60"' in svg
    assert 'rx="30"' in svg
    assert 'ry="20"' in svg

def test_ellipse_to_svg_format():
    ellipse = Ellipse(cx=10, cy=15, rx=5, ry=8, fill="blue")
    svg = ellipse.to_svg().strip()
    assert svg.startswith("<ellipse")
    assert svg.endswith("/>")
