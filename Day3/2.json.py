import json

# Task no 1: Store student information in a JSON file.
students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 20,
        "department": "CS"
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 21,
        "department": "SE"
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Initial student data stored.\n")

# Task no 2: Read data from a JSON file.
with open("students.json", "r") as file:
    students = json.load(file)

print("Current Students:")
for student in students:
    print(student)

# Task no 3: Update an existing student's information.
for student in students:
    if student["id"] == 2:
        student["age"] = 22
        student["department"] = "AI"

# Task no 4: Add a new student to the JSON file.
students.append({
    "id": 3,
    "name": "Ahmed",
    "age": 19,
    "department": "IT"
})

# Save changes
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nData updated successfully.\n")

# Display updated data
with open("students.json", "r") as file:
    updated_students = json.load(file)

print("Updated Student List:")
for student in updated_students:
    print(student)