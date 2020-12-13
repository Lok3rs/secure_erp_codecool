from model.crm import crm
from view import terminal as view

# HEADERS = ["id", "name", "email", "subscribed"]
customers = crm.data_manager.read_table_from_file(crm.DATAFILE)

def list_customers():
    print()
    customers.insert(0, crm.HEADERS)
    view.print_table(customers)


def add_customer():
    new_customer = view.get_inputs(['Name', 'Email', 'Subscribed'])
    new_customer.insert(0, crm.util.generate_id())
    customers.append(new_customer)
    return new_customer


def update_customer():
    # pF5v4wG_e_
    search_id = view.get_input('Id')
    for customer in customers:
        if customer[0] == search_id:
            new_data = view.get_inputs(['Name', 'Email', 'Subscribed'])
            new_data.insert(0, search_id)
            customers[customers.index(customer)] = new_data
            return
    view.print_error_message("Id does not exist. \n")


def delete_customer():
    search_id = view.get_input('Id')
    for customer in customers:
        if customer[0] == search_id:
            customers.remove(customer)
            return
    view.print_error_message("Id does not exist. \n")


def get_subscribed_emails():
    sub_email = []
    print("\nSubscribers emails:")
    for customer in customers:
        if int(customer[3]) == 1:
            sub_email.append(customer[2])
            print(customer[2])
    print()

    return sub_email


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

