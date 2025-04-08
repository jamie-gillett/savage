from savage import Rect

def test_rect_basic_attributes():
    rect = Rect(width=100, height=50, x=10, y=20)
    svg = rect.to_svg()
    assert 'width="100"' in svg
    assert 'height="50"' in svg
    assert 'x="10"' in svg
    assert 'y="20"' in svg

def test_rect_optional_rx_ry():
    rect = Rect(width=100, height=50, x=0, y=0, rx=5, ry=10)
    svg = rect.to_svg()
    assert 'rx="5"' in svg
    assert 'ry="10"' in svg

def test_rect_without_rx_ry():
    rect = Rect(width=80, height=40, x=5, y=5)
    svg = rect.to_svg()
    assert 'rx=' not in svg
    assert 'ry=' not in svg

def test_rect_with_styling():
    rect = Rect(width=100, height=60, x=0, y=0, fill="green", stroke="black", strokewidth="1")
    svg = rect.to_svg()
    assert 'fill="green"' in svg
    assert 'stroke="black"' in svg
    assert 'stroke-width="1"' in svg

def test_rect_svg_format():
    rect = Rect(width=10, height=10, x=0, y=0)
    svg = rect.to_svg().strip()
    assert svg.startswith("<rect")
    assert svg.endswith("/>")
