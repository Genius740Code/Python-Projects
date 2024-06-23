import time, random

z = ["True", "False"]

print("The chances of winning this game is 1/65,536 ")

a = input("True or False")
r = random.choice (z)

if a == r:
    print("Nice 1/2 chance")
    a2 = input("True or False")

    if a2 == r:
        print("Nice 1/4 chance")
        a3 = input("True or False")
        r = random.choice (z)
    else:
        print("You Lost")
        exit()
        if a3 == r:
            print("Nice 1/8 chance")
            a4 = input("True or False")
            r = random.choice (z)
        else:
            print("You Lost")
            exit()
            if a4 == r:
                print("Nice 1/16 chance")
                a5 = input("True or False")
                r = random.choice (z)
            else:
                print("You Lost")
                exit()
                if a5 == r:
                    print("Nice 1/32 chance")
                    a5 = input("True or False")
                    r = random.choice (z)                    
                else:
                    print("You Lost")
                    exit()
                    if a6 == r:
                        print("Nice 1/64 chance")
                        a6 = input("True or False")
                        r = random.choice (z)
                    else:
                        print("You Lost")
                        exit()
                        if a7 == r:
                            print("Nice 1/128 chance")
                            a7 = input("True or False")
                            r = random.choice (z)
                        else:
                            print("You Lost")
                            exit()
                            if a8 == r:
                                print("Nice 1/256 chance")
                                a8 = input("True or False")
                                r = random.choice (z)
                            else:
                                print("You Lost")
                                exit()
                                if a9 == r:
                                    print("Nice 1/512 chance")
                                    a9 = input("True or False")
                                    r = random.choice (z)
                                else:
                                    print("You Lost")
                                    exit()
                                    if a10 == r:
                                        print("Nice 1/1024 chance")
                                        a10 = input("True or False")
                                        r = random.choice (z)
                                    else:
                                        print("You Lost")
                                        exit()
                                        if a11 == r:
                                            print("Nice 1/2048 chance")
                                            a11 = input("True or False")
                                            r = random.choice (z)
                                        else:
                                            print("You Lost")
                                            exit()
                                            if a12 == r:
                                                print("Nice 1/4096 chance")
                                                a12 = input("True or False")
                                                r = random.choice (z)
                                            else:
                                                    print("You Lost")
                                                    exit()
                                                    if a13 == r:
                                                        print("Nice 1/8192 chance")
                                                        a13 = input("True or False")
                                                        r = random.choice (z)
                                                    else:
                                                            print("You Lost")
                                                            exit()
                                                            if a14 == r:
                                                                print("Nice 1/16,384‬ chance")
                                                                a14 = input("True or False")
                                                                r = random.choice (z)
                                                            else:
                                                                    print("You Lost")
                                                                    exit()
                                                                    if 15 == r:
                                                                        print("Nice 1/32,768‬ chance")
                                                                        a15 = input("True or False")
                                                                        r = random.choice (z)
                                                                    else:
                                                                        print("You Lost")
                                                                        exit()
                                                                        if 16 == r:
                                                                            print("Nice 1/65,536 chance")
                                                                            a156 = input("True or False")
                                                                            r = random.choice (z)
                                                                        else:
                                                                            print("You Lost")
                                                                            exit()
else:
    print("You Lost")
    exit()

    

