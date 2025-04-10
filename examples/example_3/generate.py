from savage import Graphic, Rect, Group

g = Graphic(width=300, height=300)

rotated_group = Group()
rotated_group.add( Rect( x=0, y=-100, width=100, height=100, fill="cornsilk", stroke="none") )
rotated_group.add( Rect( x=-100, y=0, width=100, height=100, fill="cornsilk", stroke="none") )
rotated_group.add( Rect( x=-100, y=-100, width=100, height=100, fill="crimson", stroke="none") )
rotated_group.add( Rect( x=0, y=0, width=100, height=100, fill="crimson", stroke="none") )
rotated_group.rotate(45)

translated_group = Group()
translated_group.add( rotated_group )
translated_group.translate(dx=150, dy=150)

g.add(translated_group)

g.save("output.svg")