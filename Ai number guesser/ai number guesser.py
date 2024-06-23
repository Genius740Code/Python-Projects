import random
import time

def guess_number():
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    print(f"Think of a number from {lower_bound}-{upper_bound}")
    time.sleep(1)

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        guess = int(input(f"Is it higher than {mid}? (1 for yes, 0 for no): "))

        if guess == 1:
            lower_bound = mid + 1
        elif guess == 0:
            upper_bound = mid - 1
        else:
            print("Invalid input. Please enter 1 or 0.")
            continue

    print(f"Your number is {lower_bound}.")

if __name__ == "__main__":
    guess_number()
