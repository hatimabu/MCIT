# Step 1: Get 5 numbers from the user
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nOriginal List of Numbers:", numbers)

# Step 2: Sort the list
numbers.sort()
print("\nSorted List of Numbers:", numbers)

# Step 3: Remove the largest number
largest_number = numbers.pop()
print("\nList After Removing the Largest Number:", numbers)
print("Removed Largest Number:", largest_number)

# Step 4: Calculate the average
average = sum(numbers) / len(numbers)
print("\nAverage of Remaining Numbers:", round(average, 2))
