# Ask user to enter a number
num = int(input("Enter a number: "))

# Check if number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
# Check if divisible only by 3
elif num % 3 == 0:
    print("Fizz")
# Check if divisible only by 5
elif num % 5 == 0:
    print("Buzz")
# If not divisible by 3 or 5 print the number
else:
    print(num)
