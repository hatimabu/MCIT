# Initialize a list to store lines containing the word 'error'
error_lines = []

try:
# Open and read the file line by line
    with open("data.txt", "r") as file:
        for line in file:
# Check if 'error' is in  line (case-insensitive)
            if "error" in line.lower():
                error_lines.append(line)
# Print lines  contain  word 'error'
    print("Lines containing 'error':")
    for line in error_lines:
        print(line.strip())

# Print  total number of matching lines
    print(f"\nTotal number of lines with 'error': {len(error_lines)}")

# Write  filtered lines to a new file called "errors.log"
    with open("errors.log", "w") as outfile:
        outfile.writelines(error_lines)

except FileNotFoundError:
    print("The file 'data.txt' was not found.")
