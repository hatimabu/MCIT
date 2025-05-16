d = {'name': 'Alice', 'age': 25, 'city': 'Montreal'}
keys_set = set(d.keys())

print("Keys set:", keys_set)

key_to_check = 'age'
if key_to_check in keys_set:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist.")
