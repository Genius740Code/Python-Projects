a = input("Input Something")

def isPalindrome(s):
    return s == s[::-1]

ans = isPalindrome(a)
 
if ans:
    print("Yes")
else:
    print("No")
