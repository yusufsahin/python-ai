from employee import add_employee


def main():
    while True:
        print("\n--- Employee Manager ---")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

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
        elif choice == "2":
            print("List Employees")
        elif choice == "3":
            print("Update Employee")
        elif choice == "4":
            print("Delete Employee")
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid input. Please select 1-5.")
if __name__ == '__main__':
    main()