""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util

DATAFILE = "model/crm/crm.csv"
HEADERS = ["Id", "name", "email", "subscribed"]
CUSTOMERS = data_manager.read_table_from_file(DATAFILE)
found_customer = []

ID_INDEX = 0
ID_EMAIL = 2
ID_SUB = 3

def list_of_customers():
    CUSTOMERS = data_manager.read_table_from_file(DATAFILE)
    print(CUSTOMERS)
    return CUSTOMERS

def save_customer():
    data_manager.write_table_to_file(DATAFILE, CUSTOMERS)

def add_customer(customer):
    customer.insert(ID_INDEX, util.generate_id())
    CUSTOMERS.append(customer)
    save_customer()

def if_customer_exists(search_id):
    for customer in CUSTOMERS:
        if customer[ID_INDEX] == search_id:
            global found_customer
            found_customer = customer
            return True
    return False

def update_customer(new_data):
    new_data.insert(0, found_customer[ID_INDEX])
    CUSTOMERS[CUSTOMERS.index(found_customer)] = new_data
    save_customer()

def find_customer(search_id):
    for customer in CUSTOMERS:
        if customer[ID_INDEX] == search_id:
            global found_customer
            found_customer = customer
            return customer
    return None

def delete_customer(search_id):
    temp_customer = find_customer(search_id)
    if temp_customer:
        CUSTOMERS.remove(temp_customer)
        save_customer()
        return True
    else:
        return False

def get_subscribed_emails():
    emails = []
    for customer in CUSTOMERS:
        if customer[ID_SUB] == str(1):
            emails.append(customer[ID_EMAIL])
    return emails