from model import util

date_year_index = 0
date_month_index = 1
date_day_index = 2


def print_menu(title, list_options):
    #util.clear_screen()
    list_options.append(list_options.pop(0))
    print(f"{title}:")
    for index in range(len(list_options)):
        print(f"({index + 1}) {list_options[index]}" if index != len(list_options) - 1
              else f"(0) {list_options[index]}")


def print_message(message):
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


def print_table(table):
    space_around = 2
    column_separator = "|"
    row_separator = "-"
    corner_ac = "/"
    corner_bd = "\\"
    max_column_width = [0 for element in range(len(table[0]))]

    for row in table:
        for result_index in range(len(row)):
            max_column_width[result_index] = len(row[result_index]) + space_around \
                if max_column_width[result_index] - space_around < len(row[result_index]) \
                else max_column_width[result_index]

    break_line = column_separator + column_separator.join(
        [(row_separator * max_width) for max_width in max_column_width]) + column_separator
    start_line = corner_ac + row_separator.join(
        [(row_separator * max_width) for max_width in max_column_width]) + corner_bd
    end_line = corner_bd + row_separator.join(
        [(row_separator * max_width) for max_width in max_column_width]) + corner_ac

    print(start_line)
    for row in table:
        printable_row = []
        for each_result in row:
            white_spaces = max_column_width[row.index(each_result)] - len(each_result)
            printable_row.append((white_spaces // 2 * " " if white_spaces % 2 == 0
                                  else (white_spaces // 2 + 1) * " ") + each_result +
                                 (white_spaces // 2) * " ")
        print(column_separator + column_separator.join(printable_row) + column_separator)
        print(break_line if row != table[-1] else end_line)


def get_input(label):
    return input(f"{label}: ")


def get_inputs(labels):
    answers = []
    for label in labels:
        validate = False
        while not validate:
            answer = get_input(label)
            if label == "Customer" and len(answer) != 8:
                print_error_message("Customer ID has to be 8 chars long.")
                continue
            elif label == "Price":
                try:
                    float(answer)
                except ValueError:
                    print_error_message("Price needs to be a number. Floating number has to be separated by a dot.")
                    continue
            elif label == "Date":
                date_split = answer.split("-")
                if len(date_split) != 3 or not date_split[date_year_index].isnumeric() or int(date_split[date_year_index]) < 0 \
                        or not date_split[date_month_index].isnumeric() or not date_split[date_day_index].isnumeric() \
                        or int(date_split[date_month_index]) not in range(1, 13) \
                        or int(date_split[date_day_index]) not in range(1, 32):
                    print_error_message("Wrong date provided. Has to be in format YYYY-MM-DD")
                    continue
            answers.append(answer)
            validate = True
    return answers


def print_error_message(message):
    print(f"ERROR OCCURED:\n{message}")
