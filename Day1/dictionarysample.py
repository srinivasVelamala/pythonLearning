# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Accessing dictionary values
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 20
print(student["major"])  # Output: Computer Science

student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
for key,value in student.items():
    if value == 'Alice':
        del student['name']
        break
print('After deletion')
print(student)