import turtle
sides = eval (input ("type amount sides of shape that you want to draw. The maximum number - 6:"))
#sides = input ("type amount sides of shape that you want to draw. The maximum number - 6:") - не нужно
t = turtle.Pen()
turtle.bgcolor ("black")
colors = ["orange", "red", "blue", "pink", "yellow", "white"]
for x in range(360):
    t.pencolor(colors [x % sides])
    t.forward(x * 3/sides + x)
    t.left(360 /sides + 1)
    t.width(x * sides/200)
    t.left(90)
