import time
import statistics

count = 0
total = 0

print("Welcome to Average Calculator\n")
time.sleep(1)
print("Choose an option:")
time.sleep(0.1)
print("Mean (1)")
time.sleep(0.1)
print("Median (2)")
time.sleep(0.1)
print("Mode (3)")
time.sleep(0.1)
print("Range (4)")

choice = int(input("Enter your choice: "))

if choice == 1:
    num_numbers = int(input("How many numbers? "))
    for i in range(num_numbers):
        num = int(input("Enter Number: "))
        total += num
        count += 1
    mean = total / count
    print("Mean:", mean)

elif choice == 2:
    num_numbers = int(input("How many numbers? "))
    numbers = []
    for i in range(num_numbers):
        num = int(input("Enter Number: "))
        numbers.append(num)
    median = statistics.median(numbers)
    print("Median:", median)

elif choice == 3:
    num_numbers = int(input("How many numbers? "))
    numbers = []
    for i in range(num_numbers):
        num = int(input("Enter Number: "))
        numbers.append(num)

    try:
        mode = statistics.mode(numbers)
        print("Mode:", mode)
    except statistics.StatisticsError:
        print("There is no mode.")

elif choice == 4:
    num_numbers = int(input("How many numbers? "))
    numbers = []
    for i in range(num_numbers):
        num = int(input("Enter Number: "))
        numbers.append(num)
    num_range = max(numbers) - min(numbers)
    print("Range:", num_range)

else:
    print("Invalid choice. Please choose a valid option.")
