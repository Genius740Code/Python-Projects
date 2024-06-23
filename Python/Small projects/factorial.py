def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

user_input = input("Enter a number: ")

try:
    number = int(user_input)
    result = factorial(number)
    print(f"Factorial of {number} is:", result)
except ValueError:
    print("Please enter a valid integer.")
