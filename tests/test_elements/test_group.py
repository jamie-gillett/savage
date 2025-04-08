from savage import Circle, Rect, Group

def test_group_renders_children():
    circle = Circle(cx=10, cy=10, r=5, fill="red")
    rect = Rect(width=20, height=10, x=5, y=5, fill="blue")
    group = Group(children=[circle, rect], stroke="black")

    svg = group.to_svg()

    assert svg.startswith("<g")
    assert 'stroke="black"' in svg
    assert "<circle" in svg
    assert "<rect" in svg
    assert svg.endswith("</g>")

def test_group_add_method():
    circle = Circle(cx=0, cy=0, r=10)
    group = Group()
    group.add(circle)
    
    assert len(group.content) == 1
    assert group.content[0] is circle
