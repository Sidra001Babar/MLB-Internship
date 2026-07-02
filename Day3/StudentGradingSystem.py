import json
import os

FILE_NAME = "studentss.json"


# Load records from JSON file
def loadRecords():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []
# Grading Criteria
def calculateGrade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 85:
        return "A-"

    elif marks >= 80:
        return "B+"

    elif marks >= 75:
        return "B"

    elif marks >= 70:
        return "B-"

    elif marks >= 65:
        return "C+"

    elif marks >= 60:
        return "C"

    elif marks >= 55:
        return "C-"

    elif marks >= 50:
        return "D"

    else:
        return "F"

# Save records to JSON file
def saveRecords(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)


# Add Student
def addStudent(records):

    student = {}

    student["id"] = input("Enter Student ID: ")

    # Check duplicate ID
    for record in records:
        if record["id"] == student["id"]:
            print("Student ID already exists.")
            return

    student["name"] = input("Enter Student Name: ")

    while True:
        try:
            student["age"] = int(input("Enter Student Age: "))
            break
        except ValueError:
            print("Invalid Age. Please enter a number.")

    student["subjects"] = []

    while True:
        try:
            totalSubjects = int(input("Enter Number of Subjects: "))
            if totalSubjects <= 0:
                print("Number of subjects must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid Input.")

    for i in range(totalSubjects):

        subject = {}

        subject["name"] = input(f"\nEnter Subject {i+1} Name: ")

        while True:
            try:
                marks = float(input(f"Enter Marks for {subject['name']}: "))
                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                    continue
                subject["marks"] = marks
                subject["grade"] = calculateGrade(marks)
                break
            except ValueError:
                print("Invalid Marks. Please enter a number.")

        student["subjects"].append(subject)

    records.append(student)
    saveRecords(records)

    print("Student Added Successfully.")


# Display Students
def displayStudents(records):

    if not records:
        print("No Student Records Found.")
        return

    print("\n========== Student Records ==========")

    for student in records:

        print("\n--------------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Subjects:")

        total = 0

        for subject in student["subjects"]:
            print(
                f"   Subject: {subject['name']}"
                f"\n      Marks : {subject['marks']}"
                f"\n      Grade : {subject['grade']}"
            )
            total += subject["marks"]

        average = total / len(student["subjects"])

        print("Average:", round(average, 2))
        print("--------------------------------")


# Search Student
def searchStudent(records):

    sid = input("Enter Student ID: ")

    for student in records:

        if student["id"] == sid:

            print("\nStudent Found")
            print("---------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])

            total = 0

            print("Subjects:")
            for subject in student["subjects"]:
                print(
                    f"   Subject: {subject['name']}"
                    f"\n      Marks : {subject['marks']}"
                    f"\n      Grade : {subject['grade']}"
                )
                total += subject["marks"]

            average = total / len(student["subjects"])
            print("Average:", round(average, 2))
            return

    print("Student Not Found.")


# Update Student
def updateStudent(records):

    sid = input("Enter Student ID to Update: ")

    for student in records:

        if student["id"] == sid:

            while True:

                print("\nWhat do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Subject Name")
                print("4. Subject Marks")
                print("5. Exit Update")

                try:
                    choice = int(input("Enter Choice: "))

                    # Update Name
                    if choice == 1:
                        student["name"] = input("Enter New Name: ")
                        saveRecords(records)
                        print("Name Updated Successfully.")

                    # Update Age
                    elif choice == 2:

                        while True:
                            try:
                                student["age"] = int(input("Enter New Age: "))
                                break
                            except ValueError:
                                print("Invalid Age.")

                        saveRecords(records)
                        print("Age Updated Successfully.")

                    # Update Subject Name
                    elif choice == 3:

                        subjectName = input("Enter Subject Name to Update: ")

                        found = False

                        for subject in student["subjects"]:

                            if subject["name"].lower() == subjectName.lower():

                                subject["name"] = input("Enter New Subject Name: ")

                                found = True
                                saveRecords(records)
                                print("Subject Name Updated Successfully.")
                                break

                        if not found:
                            print("Subject Not Found.")

                    # Update Subject Marks
                    elif choice == 4:

                        subjectName = input("Enter Subject Name: ")

                        found = False

                        for subject in student["subjects"]:

                            if subject["name"].lower() == subjectName.lower():

                                while True:
                                    try:
                                        marks = float(input("Enter New Marks: "))

                                        if marks < 0 or marks > 100:
                                            print("Marks should be between 0 and 100.")
                                            continue

                                        subject["marks"] = marks
                                        subject["grade"] = calculateGrade(marks)

                                        found = True
                                        saveRecords(records)

                                        print("Marks Updated Successfully.")
                                        break

                                    except ValueError:
                                        print("Invalid Marks.")

                                break

                        if not found:
                            print("Subject Not Found.")

                    elif choice == 5:
                        return

                    else:
                        print("Invalid Choice.")

                except ValueError:
                    print("Please enter a valid number.")

            return

    print("Student Not Found.")

# Delete Student
def deleteStudent(records):

    sid = input("Enter Student ID to Delete: ")

    for student in records:

        if student["id"] == sid:
            records.remove(student)
            saveRecords(records)
            print("Student Deleted Successfully.")
            return

    print("Student Not Found.")


# Main Function
def main():

    records = loadRecords()

    while True:

        print("\n========== Student Record Management ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                addStudent(records)

            elif choice == 2:
                displayStudents(records)

            elif choice == 3:
                searchStudent(records)

            elif choice == 4:
                updateStudent(records)

            elif choice == 5:
                deleteStudent(records)

            elif choice == 6:
                print("Thank You!")
                break

            else:
                print("Invalid Choice.")

        except ValueError:
            print("Please enter a valid number.")


# Program Starts Here
main()