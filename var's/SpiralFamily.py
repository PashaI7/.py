import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "orange", "purple", "blue", "green", "pink", "white", "aquamarine", "yellow", "grey"]
family = [] #clear list for names of parents
name = turtle.textinput("My family", "Type here names or press Enter for exit:")
while name!= "":
    family.append(name)
    name = turtle.textinput("My family", "Type here name or press Enter for exit:")
for x in range(100):
    t.pencolor(colors[x%len(family)]) #Switch of colors
    t.penup() #not draw only straight lines
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Times New Roman", int ((x+4)/4), "bold"))
    t.left(360/len(family)+2)
    
