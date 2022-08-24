name = input("What is your name?")
while name!= "":
    for x in range(100):
        print(name, end = " ")
    print()
    name = input("Type name one more time or press Enter for exit: ")
print("Thank you for game")
