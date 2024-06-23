score = 0

print("Welcome to my quiz")

a = input("Capital of France: ")

if a.lower() == "paris":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

print("Next question")

b = input("What cell stores DNA: ")

if b.lower() == "nucleus":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

c = input("1 + 1: ")

if c == "2":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

d = input("5 + (2 * 6): ")

if d == "17":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

print("You've got " + str(score) + "/4")
percentage = (score / 4) * 100
print("Your percentage is " + str(percentage) + "%")
