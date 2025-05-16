import re

text = "Please contact us at support@example.com or sales@company.org. You can also reach out to admin123@school.edu."

# Regular expression pattern for matching email addresses
email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'

# Find all matches
emails = re.findall(email_pattern, text)

print(emails)
