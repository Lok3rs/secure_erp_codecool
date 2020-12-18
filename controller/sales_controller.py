import model.sales.sales as sales
import model.crm.crm as crm
import controller.crm_controller as crm_controller
from view import terminal as view
from model import util

import datetime

id_index = 0
customer_index = 1
product_index = 2
price_index = 3
date_index = 4


def list_transactions():
    view.print_table([sales.HEADERS, *sales.SALES])


def add_transaction():
    view.print_message("New transaction: ")
    customer_id = view.get_input(f"{sales.HEADERS[customer_index]}")
    if not any(customer_id in customers[id_index] for customers in crm.CUSTOMERS):
        answer = view.get_input("Given customer does not exist. Type 'Y' to create").upper()
        if answer == "Y":
            view.print_message("Add customer")
            new_customer = crm_controller.add_customer()
            customer_id = new_customer[id_index]
            view.print_message(f"New customer generated with random id of {customer_id}")
    values = view.get_inputs(sales.HEADERS[product_index:])
    sales.add_transaction([customer_id, *values])
    view.print_message("Transaction added!")


def get_new_value(value):
    value = view.get_input(f"New value for {value}")
    return value


def update_transaction():
    view.print_message("Update transaction.")
    transaction_id = view.get_input("Provide transaction ID")
    sale = sales.find_by_id(transaction_id)
    if sale:
        view.print_message(f"Transaction found. Updating:\n{sales.HEADERS[id_index]}: {sale[id_index]}")
        updated_sale = []
        for header_index in range(1, len(sales.HEADERS)):
            new_option = view.get_input(f"Current value of {sales.HEADERS[header_index]}: {sale[header_index]}\n"
                                        f"New value (ENTER to keep current value)")

            updated_sale.append(new_option if len(new_option) > 0 else sale[header_index])
        sales.update_transaction(transaction_id, updated_sale)
    else:
        view.print_error_message(f"Transaction of ID {transaction_id} does not exist.")


def delete_transaction():
    view.print_message("Delete transaction.")
    transaction_id = view.get_input("Provide transaction ID")
    if view.get_input("Type 'yes' to confirm deletion").lower() == 'yes':
        view.print_message(f"Transaction {transaction_id} succesfully deleted.") if sales.remove_transaction(transaction_id) \
            else view.print_error_message(f"Transaction of ID {transaction_id} does not exist.")
    else:
        view.print_message("Delete cancelled")


def get_biggest_revenue_transaction():
    biggest_revenue_sale = sales.get_biggest_revenue_sale()
    view.print_message("Biggest revenue sale:")
    view.print_table([sales.HEADERS, *biggest_revenue_sale])


def get_biggest_revenue_product():
    product, profit = sales.get_biggest_revenue_product()
    view.print_message(f"Biggest revenue product is {product} with total profit of {profit}$.")


def get_transactions_between():
    year_index = 0
    month_index = 1
    day_index = 2
    date1_split, date2_split = ([], [])
    start_date, end_date = (datetime.date(2000, 1, 1), datetime.date(2000, 1, 1))
    first_run = True
    while len(date1_split) != 3 or len(date2_split) != 3 \
            or not date1_split[year_index] > 0 or not date2_split[year_index] > 0 \
            or date1_split[month_index] not in range(1, 13) or date2_split[month_index] not in range(1, 13) \
            or date1_split[day_index] not in range(1, 32) or date2_split[day_index] not in range(1, 32) \
            or (end_date - start_date).days < 0 \
            or date1_split[year_index] > date2_split[year_index] \
            or (
            date1_split[year_index] == date2_split[year_index] and date1_split[month_index] > date2_split[month_index]) \
            or (
            date1_split[year_index] == date2_split[year_index] and date1_split[month_index] == date2_split[month_index]
            and date1_split[day_index] > date2_split[day_index]
    ):

        view.print_message("Count transaction between dates.\nDate format YYYY-MM-DD") if first_run \
            else view.print_error_message("Wrong date provided, try again.")
        first_run = False

        try:
            date1 = view.get_input("Starting date")
            date1_split = [int(date) for date in date1.split("-")]
            date2 = view.get_input("Ending date")
            date2_split = [int(date) for date in date2.split("-")]
        except ValueError:
            continue

    start_date = datetime.date(*date1_split)
    end_date = datetime.date(*date2_split)
    sales_between = sales.get_sales_between(start_date, end_date)
    return sales_between, start_date, end_date


def count_transactions_between():
    transactions_between, start_date, end_date = get_transactions_between()
    view.print_message(f"Number of transactions found between {start_date} and {end_date}: {len(transactions_between)}")
    view.print_table([sales.HEADERS, *transactions_between]) if len(transactions_between) > 0 else None


def sum_transactions_between():
    transactions_between, start_date, end_date = get_transactions_between()
    sum_of_transactions = sum([float(price[price_index]) for price in transactions_between])
    view.print_message(f"Sum of transactions found between {start_date} and {end_date}: {sum_of_transactions}$")
    view.print_table([sales.HEADERS, *transactions_between]) if len(transactions_between) > 0 else None


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != 0:
        display_menu()
        try:
            operation = int(view.get_input("Select an operation"))
            util.clear_screen()
            run_operation(operation)
            util.wait() if operation != 0 else None
        except KeyError as err:
            view.print_error_message(err)
            util.wait()
