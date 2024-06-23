import random
import time

win = 0

num = random.randint(1, 1000000)

while True:
    ans = input("Guess a number from 1 to 1000000, press 'q' to quit: ")

    if ans == str(num):
        print("Lucky you! You win")
        win += 1

    elif ans.lower() == 'q':
        break

    else:
        time.sleep(1)
        print("Unlucky, it was:")
        time.sleep(1)
        print(num)

print("Hope you had fun")
print("You won: " + str(win) + " times")