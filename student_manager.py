import json
import os
from datetime import datetime
from student import Student

class StudentManager:
    
    def __init__(self):
        self.students = []

        if not os.path.exists("students.json"):
            with open("students.json","w") as file:
                json.dump([], file)

        self.load_students()
    def load_students(self):
        try:
            with open("students.json", "r") as file:
                self.students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []

    def save_students(self):
        with open("students.json", "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        roll_number = input("Enter Roll Number: ")

        if not roll_number.isdigit():
         print("Roll Number must contain only numbers.")
         return

        for student in self.students:
            if student["roll_number"] == roll_number :
                print ("Roll Number already exists.")
                return
            
        name = input("Enter Name: ")

        if name.strip() == "":
            print("Name cannot be empty.")
            return
    

        try:
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            marks = float(input("Enter Marks: "))

        except ValueError:
            print("Invalid input!")
            return
        
        student = Student(roll_number, name, age, department, marks)

        self.students.append(student.to_dict())

        self.save_students()

        print("Student added successfully!")
    
    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
        
        for student in self.students:
            print("----------------------------")
            print("Roll Number: ", student["roll_number"])
            print("Name: ", student["name"])
            print("Age: ", student["age"])
            print("Department:", student["department"])
            print("Marks:", student["marks"])
            print()

    def sort_students(self):
        sorted_students = sorted(self.students, key=lambda student: student["marks"], reverse=True)

        if not sorted_students:
            print("No student records found.")
            return
        
        print("\nStudents Sorted by Marks\n")

        for student in sorted_students:
            print("----------------------------")
            print("Roll Number:", student["roll_number"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])

    def top_three_students(self):
        sorted_students = sorted(self.students, key=lambda student: student["marks"], reverse=True)

        print("\nTop 3 Students\n")

        for student in sorted_students[:3]:
             print("----------------------------")
             print("Roll Number:", student["roll_number"])
             print("Name:", student["name"])
             print("Marks:", student["marks"])



    def search_student(self):
        search_roll = input("Enter Roll Number to search: ")

        for student in self.students:
            if student["roll_number"] == search_roll:
                print("Student Found")
                print("----------------------------")
                print("Roll Number:", student["roll_number"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Department:", student["department"])
                print("Marks:", student["marks"])
                return
            
        print("Student not found.")

    def update_student(self):
        update_roll = input("Enter Roll Number to update: ")

        for student in self.students:
            if student["roll_number"] == update_roll:

                student["name"] = input("Enter New Name: ")

                try:
                    student["age"] = int(input("Enter New Age: "))
                    student["department"] = input("Enter New Department: ")
                    student["marks"] = float(input("Enter New Marks: "))

                except ValueError:
                    print("Invalid input!")
                    return
                
                self.save_students()

                print("Student updated successfully!")
                return
            
        print("Student not found.")




    def delete_student(self):
        delete_roll = input("Enter Roll Number to delete: ")
        
        for student in self.students:
            if student["roll_number"] == delete_roll:

                self.students.remove(student)

                self.save_students()

                print("Student deleted successfully!")
                return
        
        print("Student not found.")

    def generate_report(self):
        with open("report.txt", "w") as file:

            file.write("=====================================\n")
            file.write("      STUDENT RECORD REPORT\n")
            file.write("=====================================\n\n")

            current_time = datetime.now().strftime("%d %B %Y %I:%M:%S %p")
            file.write(f"Report Generated: {current_time}\n\n")

            file.write(f"Total Students: {len(self.students)}\n\n")

            departments = {}

            for student in self.students:
                dept = student["department"]

                if dept in departments:
                    departments[dept] += 1
                else:
                    departments[dept] = 1
                
            file.write("Students in Each Department:\n")

            for dept, count in departments.items():
                file.write(f"{dept}: {count}\n")

            file.write("\n")

            if self.students:
                highest = max(self.students, key=lambda student: student["marks"])

                file.write("Highest Scoring Student:\n")
                file.write(f"Roll Number: {highest['roll_number']}\n")
                file.write(f"Name: {highest['name']}\n")
                file.write(f"Marks: {highest['marks']}\n")
            
        print("Report generated successfully!")

        




