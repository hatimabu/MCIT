students = {
    "Alice": [85, 90, 78],
    "Bob": [72, 88, 91],
}

# Add a new student
students["Charlie"] = [95, 85, 87]

# Update a student's grades (e.g., add a new grade for Bob)
students["Bob"].append(89)

# Calculate and print average grade for each student
for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s average grade: {average:.2f}")
