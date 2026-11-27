from datetime import datetime


def get_menu_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a whole number.")
        return None


def get_non_empty_input(message):
    value = input(message).strip()

    while value == "":
        print("This field cannot be empty.")
        value = input(message).strip()

    return value


def get_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Enter a value greater than zero.")

        except ValueError:
            print("Please enter a valid number.")


def get_positive_int(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Enter a whole number greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_value_in_range(message, minimum, maximum):
    while True:
        try:
            value = float(input(message))

            if minimum <= value <= maximum:
                return value

            print("Enter a value between", minimum, "and", maximum)

        except ValueError:
            print("Please enter a valid number.")


def get_date(message):
    while True:
        value = input(message).strip()

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value

        except ValueError:
            print("Enter the date in YYYY-MM-DD format.")


def get_month(message):
    while True:
        value = input(message).strip()

        try:
            datetime.strptime(value, "%Y-%m")
            return value

        except ValueError:
            print("Enter the month in YYYY-MM format.")


def confirm_action(message):
    answer = input(message + " (y/n): ").strip().lower()

    while answer not in ["y", "n"]:
        print("Enter y or n.")
        answer = input(message + " (y/n): ").strip().lower()

    return answer == "y"


def format_money(amount):
    return "Rs. " + format(amount, ".2f")


def format_energy(amount):
    return format(amount, ".2f") + " kWh"
