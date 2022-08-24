import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("Amount of sides","How many sides will be in your spiral?(2-6):", 4, 2, 6))
colors = ["white", "orange", "red", "green", "yellow", "blue"]
for m in range (100):
    t.forward(m*4)
    position = t.position() #Запомнить угол спирали
    heading = t.heading() #Запомнить напрвление следования
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0]) #Вернуться в положение x спирали
    t.sety(position[1]) #Вернуться в положение у спирали
    t.setheading(heading) #Указать на направление большой спирали
    t.left(360/sides + 2) #Нацелиться на следующую точку

