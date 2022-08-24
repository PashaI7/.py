driving_age = eval(input("What is a minimal age for drive a car in your country?:"))
your_age = eval(input("How old are you?"))
if your_age >= driving_age:
    print("You are old enough to drive a car!")
else:
        if driving_age - your_age > 4:
            print("You can get a driving license after", driving_age - your_age, "age.")
            if driving_age - your_age == 1:
                print("you can't drive a car yet during", driving_age - your_age, "age.")
        if driving_age - your_age!= 1 and driving_age - your_age <= 4:
            print("Sorry, you can't drive a car during", driving_age - your_age, "age.")