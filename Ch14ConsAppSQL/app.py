from employee import add_employee, list_employees, update_employee, delete_employee, get_employee_by_id


def main():
    while True:
        print("\n--- Employee Manager ---")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Get Employee By Id")
        print("6. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            name = input("Enter employee name: ")
            department = input("Enter employee department: ")
            try:
                salary = float(input("Enter employee salary: "))
                if salary <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid salary")
                continue
            add_employee(name, department, salary)
            print("Employee added successfully")
        elif choice == "2":
            print("List Employees")
            list_employees()
        elif choice == "3":
            print("Update Employee")
            emp_id = input("Enter employee id: ")
            name = input("Enter employee name: ")
            department = input("Enter employee department: ")
            salary = float(input("Enter employee salary: "))
            print("Updating Employee...")
            update_employee(emp_id,name, department, salary)
            print("Employee updated successfully")
        elif choice == "4":
            emp_id = int(input("Enter employee id: "))
            print("Deleting Employee...")
            delete_employee(emp_id)
            print("Employee Deleted!")
        elif choice == "5":
            emp_id = int(input("Enter employee id: "))
            employee = get_employee_by_id(emp_id)
            if employee is not None:
                print(f"ID : {employee[0]}, Name : {employee[1]},Dept:{employee[2]}, Salary : {employee[3]}")
            else:
                print("Employee not found")
        elif choice=="6":
            print("Good Bye...")
            break
        else:
            print("Invalid input. Please select 1-5.")
if __name__ == '__main__':
    main()