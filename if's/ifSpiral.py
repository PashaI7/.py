answer = input ("Do you want to see a spiral? y/n: ")
if answer == 'y':
    print("in progress...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("ready!")
if answer == 'n':
   print("Unfortunately u don't want")
