from model.hr import hr
from view import terminal as view


def list_employees():
    view.print_message("List of employees:\n")
    table = hr.list_employees()
    view.print_table(table)


def add_employee():
    view.print_message("New employee: ")
    new_employee = view.get_inputs([hr.HEADERS[hr.NAME_INDEX], hr.HEADERS[hr.DATE_OF_BIRTH_INDEX], hr.HEADERS[hr.DEPARTMENT_INDEX], hr.HEADERS[hr.CLEARANCE_INDEX]])
    hr.add_employee(new_employee)
    view.print_message("Employee added!")

def update_employee():
    list_employees()
    view.print_message("Update employee.")
    updated_employee_id = view.get_input("Provide employee ID: ")
    updated_employee_data = view.get_inputs([hr.HEADERS[hr.NAME_INDEX], hr.HEADERS[hr.DATE_OF_BIRTH_INDEX], hr.HEADERS[hr.DEPARTMENT_INDEX], hr.HEADERS[hr.CLEARANCE_INDEX]])
    hr.update_employee(updated_employee_id, updated_employee_data)
    view.print_message("Employee updated!")

def delete_employee():
    list_employees()
    view.print_message("Delete employee.")
    deleted_employee_id = view.get_input("Provide employee ID: ")
    hr.delete_employee(deleted_employee_id)
    view.print_message("Employee deleted!")


def get_oldest_and_youngest():
    hr.get_oldest_and_youngest()
    view.print_message(f"The oldest employee is {hr.get_oldest_and_youngest()[0]} and the youngest employee is {hr.get_oldest_and_youngest()[1]}.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_message("Employees with at least the given clearance level.")
    celearance_level = int(view.get_input("Provide clearance level: "))
    hr.count_employees_with_clearance(celearance_level)
    view.print_message(f"There are {hr.count_employees_with_clearance(celearance_level)} employees with at least the given clearance level.")


def count_employees_per_department():
    hr.count_employees_per_department()
    view.print_message(f"There are following numbers of employees per department: {hr.count_employees_per_department()}.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
