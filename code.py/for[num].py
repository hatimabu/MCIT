price = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    if num < 0:
        print("Negative numbers are not allowed. Please enter a positive number.")
    else:
        price.append(num)
total = sum(price)
average = total / len(price)
highest = max(price)
lowest = min(price)
items_over_20 = sum(1 for price in price if price > 20)
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"numbers of items over 20: {items_over_20}")
