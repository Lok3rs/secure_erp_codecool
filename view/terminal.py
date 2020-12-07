def print_menu(title, list_options):
    print(f"{title}:")
    for index in range(len(list_options)):
        print(f"({index + 1}) {list_options[index]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


def print_table(table):
    break_line = "|" + "".join([
        "-" * 14 + "|" if len(table[0][i]) % 2 == 0
        else "-" * 15 + "|"
        for i in range(len(table[0]))
    ])
    dashes = "-" * (len(break_line) - 2)
    print(f"/{dashes}\\")
    for row in table:
        print_row = "|" + "".join([
            "{:^14}|".format(result) if len(table[0][row.index(result)]) % 2 == 0
            else "{:^15}|".format(result)
            for result in row
        ])
        print(print_row)
        print(break_line if row != table[-1] else f"\\{dashes}/")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(f"{label}: ")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    return [input(f"{label}: ") for label in labels]



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"ERROR OCCURED\n{message}")
