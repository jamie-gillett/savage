from savage import Polygon

def test_polygon_basic_attributes():
    polygon = Polygon(points=[10, 20, 30, 40, 50, 60], fill="red", stroke="blue")
    svg = polygon.to_svg()

    assert '<polygon' in svg
    assert 'points="10,20 30,40 50,60"' in svg

def test_polygon_with_invalid_points():
    try:
        polygon = Polygon(points=[10, 20, 30, 40, 50])  # Odd number of points
    except ValueError as e:
        assert str(e) == "Points must contain an even number of elements (x, y pairs)."

def test_polygon_svg_format():
    polygon = Polygon(points=[5, 10, 15, 20, 25, 30])
    svg = polygon.to_svg().strip()

    assert svg.startswith("<polygon")
    assert svg.endswith("/>")
