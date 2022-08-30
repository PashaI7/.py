rainy = input("What is the weather? Rain is going? (y/n)").lower()
cold = input("At the outside so cold? (y/n)").lower()
if (rainy == 'y' and cold == 'y'):
    print ("it is the beat way on this weather to wear a smth warmer for example coat.")
elif (rainy == 'y' and cold != 'y'):
    print ("Take a raindow!")
elif (rainy != 'y' and cold == 'y'):
    print ("You could wear a jacket!")
elif (rainy != 'y' and cold != 'y'):
    print ("Today is weather fine! You need to take a cream for protect your leather!")
    