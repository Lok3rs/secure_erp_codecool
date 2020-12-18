""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util
from typing import List
import datetime

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
SALES = data_manager.read_table_from_file(DATAFILE)

id_index = 0
customer_index = 1
product_index = 2
price_index = 3
date_index = 4


def get_transactions():
    return data_manager.read_table_from_file(DATAFILE)


def save_to_file(table):
    data_manager.write_table_to_file(DATAFILE, table)


def generate_transaction_id():
    return util.generate_id()


def add_transaction(values: List):
    SALES.append([generate_transaction_id(), *values])
    save_to_file(SALES)


def find_by_id(transaction_id):
    for sale in SALES:
        if sale[id_index] == transaction_id:
            return sale
    return False


def remove_transaction(transaction_id):
    sale = find_by_id(transaction_id)
    if sale:
        SALES.remove(sale)
        save_to_file(SALES)
        return True
    return False


def update_transaction(transaction_id, updated_sale):
    sale = find_by_id(transaction_id)
    if sale:
        SALES[SALES.index(sale)] = [sale[id_index], *updated_sale]
        save_to_file(SALES)
        return True
    return False


def get_biggest_revenue_sale():
    biggest_price = max([float(sale[price_index]) for sale in SALES])
    return list(filter(lambda sale: float(sale[price_index]) == biggest_price, SALES))


def get_biggest_revenue_product():
    products = set([sale[product_index] for sale in SALES])
    profit_dict = {}
    for product in products:
        profit_dict[product] = sum(
            [float(sale[price_index]) if sale[product_index] == product else 0 for sale in SALES])
    biggest_profit = max(profit_dict.values())
    for product, profit in profit_dict.items():
        if profit == biggest_profit:
            return product, profit


def get_sales_between(start_date, end_date):
    delta = end_date - start_date
    dates_between = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    sales_between = []
    for sale in SALES:
        transaction_date = datetime.date(*[int(date) for date in sale[date_index].split("-")])
        if any(date == transaction_date for date in dates_between):
            sales_between.append(sale)
    return sales_between
