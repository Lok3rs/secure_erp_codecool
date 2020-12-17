""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
ID_INDEX = 0
NAME_INDEX = 1
DATE_OF_BIRTH_INDEX = 2
DEPARTMENT_INDEX = 3
CLEARANCE_INDEX = 4

def list_employees():
    table = data_manager.read_table_from_file(DATAFILE)
    table.insert(0, HEADERS)
    return table


def add_employee(new_employee):
    new_employee.insert(0, util.generate_id())
    new_table = data_manager.read_table_from_file(DATAFILE)
    new_table.append(new_employee)
    data_manager.write_table_to_file(DATAFILE, new_table, ";")


def update_employee(updated_employee_name, updated_employee_data):
    new_table = data_manager.read_table_from_file(DATAFILE)
    for employee in new_table:
        if employee[NAME_INDEX] == updated_employee_name:
            updated_employee_data.insert(0, employee[ID_INDEX])
            new_table[new_table.index(employee)] = updated_employee_data
    data_manager.write_table_to_file(DATAFILE, new_table, ";")


def delete_employee(deleted_employee_name):
    new_table = data_manager.read_table_from_file(DATAFILE)
    for employee in new_table:
        if employee[NAME_INDEX] == deleted_employee_name:
            new_table.pop(new_table.index(employee))
    data_manager.write_table_to_file(DATAFILE, new_table, ";")


def get_oldest_and_youngest():
    pass


def get_average_age():
    pass


def next_birthdays():
    pass


def count_employees_with_clearance(celearance_level):
    table = data_manager.read_table_from_file(DATAFILE)
    employees_with_clearance_level = 0
    for employee in table:
        if int(employee[CLEARANCE_INDEX]) >= celearance_level:
            employees_with_clearance_level += 1
    return employees_with_clearance_level


def count_employees_per_department():
    table = data_manager.read_table_from_file(DATAFILE)
    employees_per_department = {}
    for employee in table:
        if employee[DEPARTMENT_INDEX] not in employees_per_department:
            employees_per_department[employee[DEPARTMENT_INDEX]] = 1
        elif employee[DEPARTMENT_INDEX] in employees_per_department:
            employees_per_department[employee[DEPARTMENT_INDEX]] += 1
    return employees_per_department