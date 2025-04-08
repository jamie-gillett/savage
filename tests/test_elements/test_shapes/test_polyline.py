from savage import Polyline

def test_polyline_basic_attributes():
    polyline = Polyline(points=[10, 20, 30, 40, 50, 60], fill="green", stroke="black")
    svg = polyline.to_svg()

    assert '<polyline' in svg
    assert 'points="10,20 30,40 50,60"' in svg
    assert 'fill="green"' in svg
    assert 'stroke="black"' in svg

def test_polyline_with_invalid_points():
    try:
        polyline = Polyline(points=[10, 20, 30, 40, 50])  # Odd number of points
    except ValueError as e:
        assert str(e) == "Points must contain an even number of elements (x, y pairs)."

def test_polyline_svg_format():
    polyline = Polyline(points=[5, 10, 15, 20, 25, 30])
    svg = polyline.to_svg().strip()

    assert svg.startswith("<polyline")
    assert svg.endswith("/>")
