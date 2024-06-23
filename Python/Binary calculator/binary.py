import time

print("Hello, welcome to binary converter")
time.sleep(2)
print("Would you like to convert a denary to binary or binary to denary\n")
time.sleep(2.5)
print("1=Binary to Denary\n")
answer = input("2=Denary to Binary\n")

if answer == "1":
    binary = input("Input a number in binary:")
    denary = 0
    for digit in binary:  
        denary = denary * 2 + int(digit)  
    print("Your denary number is: " + str(denary))
else: 
    denary = int(input("Input a denary number:"))  
    binary = ""  
    while denary > 0:
        binary = str(denary % 2) + binary
        denary = denary // 2  
    print("Your binary number is: " + binary)
