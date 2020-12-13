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
    transaction = [sales.util.generate_id()]
    view.print_message(f"{sales.HEADERS[id_index]}: {transaction[id_index]}")
    customer_id = view.get_input(f"{sales.HEADERS[customer_index]}")
    if not any(customer_id in customers[id_index] for customers in crm.CUSTOMERS):
        answer = view.get_input("Given customer does not exist. Type 'Y' to create").upper()
        if answer == "Y":
            view.print_message("Add customer")
            new_customer = crm_controller.add_customer()
            customer_id = new_customer[id_index]
            view.print_message(f"New customer generated with random id of {customer_id}")
    transaction.extend(customer_id)
    transaction.extend(view.get_inputs(sales.HEADERS[product_index:]))
    sales.SALES.append(transaction)
    sales.data_manager.write_table_to_file(sales.DATAFILE, sales.SALES)
    view.print_message("Transaction added!")


def get_transaction_by_id(option):
    transaction_id = view.get_input("Provide transaction ID")
    for sale in sales.SALES:
        if sale[id_index] == transaction_id and option == "update":
            view.print_message(f"Transaction found. Updating:\n{sales.HEADERS[id_index]}: {sale[id_index]}")
            for header_index in range(1, len(sales.HEADERS)):
                new_option = view.get_input(f"Current value of {sales.HEADERS[header_index]}: {sale[header_index]}\n"
                                            f"New value (ENTER to keep current value)")
                sales.SALES[sales.SALES.index(sale)][header_index] = new_option if len(new_option) > 0 \
                    else sales.SALES[sales.SALES.index(sale)][header_index]
            sales.data_manager.write_table_to_file(sales.DATAFILE, sales.SALES)
        elif sale[id_index] == transaction_id and option == "delete":
            choose = view.get_input("Confirm deletion by typing 'yes':").lower()
            if choose == "yes":
                sales.SALES.remove(sale)
                sales.data_manager.write_table_to_file(sales.DATAFILE, sales.SALES)
                view.print_message("Delete completed.")
            else:
                view.print_message("Delete canceled.")
        elif sale[id_index] == transaction_id:
            view.print_error_message("Wrong option chosen.")
    view.print_error_message(f"Transaction of ID {transaction_id} doesn't exist.") \
        if not any(transaction_id in sale[id_index] for sale in sales.SALES) else None


def update_transaction():
    view.print_message("Update transaction.")
    get_transaction_by_id("update")


def delete_transaction():
    view.print_message("Delete transaction.")
    get_transaction_by_id("delete")


def get_biggest_revenue_transaction():
    biggest_sales = []
    biggest_price = 0
    for sale in sales.SALES:
        if float(sale[price_index]) > biggest_price:
            biggest_price = float(sale[price_index])
            biggest_sales = [sale]
        elif float(sale[price_index]) == biggest_price:
            biggest_sales.append(sale)
    view.print_message("Biggest revenue sale:")
    view.print_table([sales.HEADERS, *biggest_sales])


def get_biggest_revenue_product():
    products = set([sale[product_index] for sale in sales.SALES])
    profit_dict = {}
    for product in products:
        profit_dict[product] = sum([float(sale[price_index]) if sale[product_index] == product else 0 for sale in sales.SALES])
    biggest_profit = max(profit_dict.values())
    for product, profit in profit_dict.items():
        if profit == biggest_profit:
            view.print_message(f"Biggest revenue product is {product} with a total profit of {profit}$")


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
            date1_split[year_index] == date2_split[year_index] and date1_split[month_index] > date2_split[month_index])\
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
    delta = end_date - start_date
    dates_between = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    sales_between = []
    for sale in sales.SALES:
        transaction_date = datetime.date(*[int(date) for date in sale[date_index].split("-")])
        if any(date == transaction_date for date in dates_between):
            sales_between.append(sale)
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
