# Create student_info
student_info = {"name": "Lucia", "age": 50, "major": "I don't know"}

# Print name and age
print("Name", student_info["name"], "Age", student_info["age"])

# Add new key email
student_info["email"] = "lucia@gmail.com"
print(student_info.items())

# Update the age
student_info["age"] = 51
print(student_info.items())

# Remove the key major
del student_info["major"]
print(student_info.items())
