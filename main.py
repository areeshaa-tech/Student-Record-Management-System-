from colorama import Fore, Style, init
from student_manager import StudentManager
init()

manager = StudentManager()

while True:
    print(Fore.MAGENTA +"\n========== STUDENT RECORD SYSTEM ==========")
    print(Fore.LIGHTMAGENTA_EX +"1. Add Student")
    print(Fore.LIGHTMAGENTA_EX +"2. View Students")
    print(Fore.LIGHTMAGENTA_EX +"3. Search Student")
    print(Fore.LIGHTMAGENTA_EX +"4. Update Student")
    print(Fore.LIGHTMAGENTA_EX +"5. Delete Student")
    print(Fore.LIGHTMAGENTA_EX +"6. Sort Student by Marks")
    print(Fore.LIGHTMAGENTA_EX +"7. Display Top 3 Students")
    print(Fore.LIGHTMAGENTA_EX +"8. Generate Report")
    print(Fore.RED + "9. EXIT")
    print(Style.RESET_ALL)


    choice = input("Enter your choice: ")
    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.update_student()

    elif choice == "5":
        manager.delete_student()

    elif choice == "6":
        manager.sort_students()

    elif choice == "7":
        manager.top_three_students()

    elif choice == "8":
        manager.generate_report()
        
    elif choice == "9":
        print("Thank you for using Student Record System!")
        break
    else:
        print("Invalid choice. Please try again.")
        