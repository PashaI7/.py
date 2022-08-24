import turtle
t = turtle.Pen()
number  = int(turtle.numinput("Amount of circles or sides", "Amount of circles or sides", 6))
shape = turtle.textinput("What type of figure?", "Type 'r' - rosette or 'p' - polygon: ")
for x in range(number):
    if shape == 'r':
        t.circle(100)
        t.left(100 + 0.5)
    else:
        t.forward(150)
        t.left(360/number)
    
    
    