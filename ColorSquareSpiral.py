import turtle
t = turtle.Pen()
colors = ["purple", "orange", "white", "aquamarine", "red", "blue", "brown", "green"]
sides = int (turtle.numinput ("How many sides", "Type amount sides of shape that you want to draw(1-8)?", 4 ,1 ,8))
turtle.bgcolor ("black")
for x in range(360):
    t.pencolor(colors [x % sides])
    t.circle(x * 3 / sides + x)
    t.left(360 / sides + 1)
