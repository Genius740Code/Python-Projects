import time

d, a = 0, 0

b = int(input("Enter your timetable number: "))
c = int(input("Enter your amount of numbers: "))


for i in range(c):
    a+=1
    d+=1
    print(b, "x", d, "=", b*a) 
    time.sleep(0.05)
    
