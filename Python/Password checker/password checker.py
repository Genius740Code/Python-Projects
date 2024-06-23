import re

def check_password_strength(password):
    # Define criteria for a strong password
    length_check = len(password) >= 8
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    digit_check = any(char.isdigit() for char in password)
    special_char_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Evaluate the password based on criteria
    if length_check and uppercase_check and lowercase_check and digit_check and special_char_check:
        return "Strong Password"
    else:
        return "Weak Password"

user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print(f"Password Strength: {result}")
