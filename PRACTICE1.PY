students = {}

def add_student(roll_no, name, address):
    students[roll_no] = {'name': name, 'address': address}

def update_student(roll_no, name=None, address=None):
    if roll_no in students:
        if name:
            students[roll_no]['name'] = name
        if address:
            students[roll_no]['address'] = address

def delete_student(roll_no):
    if roll_no in students:
        del students[roll_no]

def fetch_students():
    return [{{'roll_no': roll_no}, **info} for roll_no, info in students.items()]

#take user input for roll number, name, and addresss and make it menu driven
def menu():
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Fetch Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            address = input("Enter address: ")
            add_student(roll_no, name, address)
            print(f"Student {name} added successfully.")
        
        elif choice == '2':
            roll_no = input("Enter roll number to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            update_student(roll_no, name if name else None, address if address else None)
            print(f"Student {roll_no} updated successfully.")
        
        elif choice == '3':
            roll_no = input("Enter roll number to delete: ")
            delete_student(roll_no)
            print(f"Student {roll_no} deleted successfully.")
        
        elif choice == '4':
            students_list = fetch_students()
            if students_list:
                for student in students_list:
                    print(student)
            else:
                print("No students found.")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
if _name_ == "_main_":
    menu()
    # Uncomment the line below to see the current state of students
    print(students)