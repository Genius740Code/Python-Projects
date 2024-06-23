import random

a = 0

r = random.randint(1, 100)

while True:
    a = int(input("Enter a number between 1 and 100: "))
    
    if a > r:
        print("Too high")
        a = a+1
    elif a < r:
        print("Too low")
        a = a+1
    else:
        print("You got it in " + str(a) + " moves!")
        break
