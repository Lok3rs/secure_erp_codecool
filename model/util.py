import random
import string
import os


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    generated_id = [
        *[random.choice(string.ascii_lowercase) for i in range(number_of_small_letters)],
        *[random.choice(string.ascii_uppercase) for i in range(number_of_capital_letters)],
        *[str(random.randint(0, 9)) for i in range(number_of_digits)],
        *[random.choice(allowed_special_chars) for i in range(number_of_special_chars)]
    ]
    random.shuffle(generated_id)
    return "".join(generated_id)


def clear_screen():
    return os.system("cls || clear")


def wait():
    input("Type ENTER to continue...")
