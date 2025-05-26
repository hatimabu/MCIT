# List of tuples containing student names and scores
students = [("Alice", 85), ("Bob", 78), ("Charlie", 92)]

# Convert list of tuples into a dictionary
student_dict = dict(students)

# Filter students with scores above 80 using dictionary comprehension
top_students = {name: score for name, score in student_dict.items() if score > 80}

# Extract just  names using list comprehension
top_names = [name for name in top_students]

# Print  full dictionary
print("Student Dictionary:", student_dict)

# Print students  score above 80
print("Top Students (score > 80):", top_students)

# Print only  names of top students
print("Names of Top Students:", top_names)