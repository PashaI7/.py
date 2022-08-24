import turtle
t = turtle.Pen()
turtle.bgcolor("silver")
colors = ["purple", "white", "orange", "red", "green", "black", "yellow", "blue"]
sides = int (turtle.numinput("How many sides", "How many side you want to draw (1-8)?",4 , 1, 8))
for x in range (360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width (x * sides / 200)
    
