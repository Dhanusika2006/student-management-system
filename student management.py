# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    mark = input("Enter mark: ")

    student = {
        "name": name,
        "age": age,
        "mark": mark
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
    else:
        print("\n Student List:")
        for i, s in enumerate(students, start=1):
            print(f"{i}. Name: {s['name']}, Age: {s['age']}, Mark: {s['mark']}")
        print()


def search_student():
    search_name = input("Enter name to search: ")
    found = False

    for s in students:
        if s["name"].lower() == search_name.lower():
            print("Student Found:")
            print(f"Name: {s['name']}, Age: {s['age']}, Mark: {s['mark']}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")


while True:
    print("====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")