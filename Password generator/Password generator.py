import random
import string

def generate_password(length, num_symbols, num_numbers, num_uppercase, num_lowercase):
    symbols = '!@#$%^&*()_-+=<>?/[]{},.'
    all_characters = string.ascii_letters + string.digits + symbols
    
    # Generate required number of characters of each type
    symbols_part = ''.join(random.choice(symbols) for _ in range(num_symbols))
    numbers_part = ''.join(random.choice(string.digits) for _ in range(num_numbers))
    uppercase_part = ''.join(random.choice(string.ascii_uppercase) for _ in range(num_uppercase))
    lowercase_part = ''.join(random.choice(string.ascii_lowercase) for _ in range(num_lowercase))
    
    # Generate remaining characters to meet the desired length
    remaining_length = length - (num_symbols + num_numbers + num_uppercase + num_lowercase)
    remaining_part = ''.join(random.choice(all_characters) for _ in range(remaining_length))
    
    # Combine all parts and shuffle the characters
    password = symbols_part + numbers_part + uppercase_part + lowercase_part + remaining_part
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    
    return shuffled_password

def get_user_input():
    length = int(input("Enter the total length of the password: "))
    num_symbols = int(input("Enter the number of symbols: "))
    num_numbers = int(input("Enter the number of numbers: "))
    num_uppercase = int(input("Enter the number of uppercase letters: "))
    num_lowercase = int(input("Enter the number of lowercase letters: "))
    
    return length, num_symbols, num_numbers, num_uppercase, num_lowercase

def main():
    length, num_symbols, num_numbers, num_uppercase, num_lowercase = get_user_input()
    
    if length < (num_symbols + num_numbers + num_uppercase + num_lowercase):
        print("Error: Total length is less than the sum of specified character types.")
        return
    
    password = generate_password(length, num_symbols, num_numbers, num_uppercase, num_lowercase)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
