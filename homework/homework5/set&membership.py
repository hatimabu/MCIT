primes = {2, 3, 5, 7, 11, 13, 17, 19}

num = int(input("Enter a number to check if it's prime: "))
if num in primes:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not in the set of primes.")
