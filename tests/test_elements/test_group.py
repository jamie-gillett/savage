from savage import Circle, Rect, Group

def test_group_renders_children():
    circle = Circle(cx=10, cy=10, r=5, fill="red")
    rect = Rect(width=20, height=10, x=5, y=5, fill="blue")
    group = Group(content=[circle, rect], stroke="black")

    svg = group.to_svg()

    assert svg.strip().startswith("<g")
    assert 'stroke: black;' in svg
    assert "    <circle" in svg
    assert "    <rect" in svg
    assert svg.strip().endswith("</g>")

def test_group_add_method_appends_to_content():
    circle = Circle(cx=0, cy=0, r=10)
    group = Group()
    group.add(circle)

    assert group.content == [circle]

def test_group_add_open_tag_svg_has_newline():
    group = Group()
    open_tag = group.add_open_tag_svg()
    assert open_tag.endswith("\n")
    assert open_tag.startswith("<g")

def test_group_add_content_svg_renders_nested_elements():
    circle = Circle(cx=5, cy=5, r=5, fill="green")
    rect = Rect(width=10, height=5, x=2, y=2, fill="yellow")
    group = Group(content=[circle, rect])

    content = group.add_content_svg()

    assert "<circle" in content
    assert "<rect" in content
    assert content.startswith("  ")
    assert content.count("\n") == 2
