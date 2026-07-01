def studentGradingSystem(student):

    total = 0

    print("\n------ Student Report ------")
    print("Student Name:", student["name"])

    for subject in student["subjects"]:
        print(f"{subject['name']}: {subject['marks']}")
        total += subject["marks"]

    average = total / len(student["subjects"])

    # Assign grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    print("Average:", round(average, 2))
    print("Grade:", grade)

# -----------------------
student = {
    "name": "",
    "subjects": []
}

student["name"] = input("Enter Student Name: ")

num_subjects = int(input("Enter Number of Subjects: "))

for i in range(num_subjects):
    subject = {
        "name": "",
        "marks": 0
    }

    subject["name"] = input(f"\nEnter Subject {i+1} Name: ")
    subject["marks"] = float(input(f"Enter marks for {subject['name']}: "))

    student["subjects"].append(subject)

# Function Call
studentGradingSystem(student)