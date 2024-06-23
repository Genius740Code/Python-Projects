def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

result = prime_numbers_in_range(start_range, end_range)
print(f"Prime numbers in the range {start_range} to {end_range}: {result}")
