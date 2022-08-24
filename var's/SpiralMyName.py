import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = [ "purple", "white", "orange", "red", "grey", "green", "pink", "blue"]
your_name = turtle.textinput ("Write your name here", "What is your name?")
for x in range (100):
    t.pencolor(colors [x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Times New Roman", int((x+4)/4),"bold"))
    t.left(92)
    
                               
