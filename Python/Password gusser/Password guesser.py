import time,sys,random,subprocess



print("Welcome to Password Guesser")
time.sleep(1)
print("Can you guess the password?")
time.sleep(1)
ans = input("Enter Password...")


if ans == "H*17hjA99&&Z":
    print("Password guessed\n")
    print("Opening File")
    subprocess.call("Buckle my shoe.py", shell=True) #Project to open
    

elif ans == "no":
    print("Dam")

else:
    print("Password Incorrect")
