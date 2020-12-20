from model.crm import crm
from view import terminal as view

HEADERS = ["id", "name", "email", "subscribed"]

ID_INDEX = 0
ID_NAME = 1

def list_customers():
    temp_customers = crm.list_of_customers()
    temp_customers.insert(0, HEADERS)
    view.print_table(temp_customers)


def add_customer():
    new_customer = view.get_inputs(['Name', 'Email', 'Subscribed'])
    if validate_email(new_customer[ID_NAME]):
        crm.add_customer(new_customer)
    else:
        view.print_error_message("Wrong email.")

def validate_email(email):
    email_split = email.split("@")
    return len(email_split) == 2 and "." in email_split[1]

def update_customer():

    search_id = view.get_input('Id')
    if crm.if_customer_exists(search_id):
        print("Give the new data.")
        new_data = view.get_inputs(['Name', 'Email', 'Subscribed'])
        crm.update_customer(new_data)
    else:
        view.print_error_message("Id does not exist. \n")


def delete_customer():
    search_id = view.get_input('Id')
    if crm.delete_customer(search_id):
        view.print_message('Deletion was successfull.')
    else:
        view.print_error_message("Id does not exist. \n")


def get_subscribed_emails():
    print("\nSubscribers emails:")
    for email in crm.get_subscribed_emails():
        print(email)
    print()

def run_operation(option):
    if option == 1:
        add_customer()
    elif option == 2:
        list_customers()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "Add new customer",
               "List customers",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)

