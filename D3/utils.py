from datetime import datetime

#Enter menu choice within 
def enter_menu_choice(message: str) -> int:
  print(message)

  # Keep prompting until a whole number strictly between 0 and 10 is entered
  while True:
    raw_choice = input("Enter a choice: ")

    if not raw_choice.isdigit():
      print("Invalid input. Enter a whole number between 0 and 10.")
      continue

    choice = int(raw_choice)

    # Exclude 0 and 10 (valid values are 1 through 9)
    if choice <= 0 or choice >= 10:
      print("Choice must be greater than 0 and less than 10. Try again.")
      continue

    return choice
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

#Get email in the right format

def get_valid_email(message: str) -> str:
  print(message)

  while True:
    email = input()

    # Require exactly one '@' and no spaces
    if email.count("@") != 1 or " " in email:
      print("Invalid email format. Try again.")
      continue

    local, domain = email.split("@")

    # Check that the local part is not empty and does not start or end with a dot
    if local == "" or local[0] == "." or local[-1] == ".":
      print("Invalid email format. Try again.")
      continue

    # Require at least one dot in the domain and no leading or trailing dot
    if "." not in domain or domain[0] == "." or domain[-1] == ".":
      print("Invalid email format. Try again.")
      continue

    print("Email accepted.")
    return email

#Get password in the right format 
def prompt_valid_password(message: str) -> str:
  print(message)

  while True:
    password = input()

    has_min_length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if has_min_length and has_upper and has_lower:
      print("Password accepted.")
      return password

    missing = []
    if not has_min_length:
      missing.append("at least 8 characters")
    if not has_upper:
      missing.append("one uppercase letter")
    if not has_lower:
      missing.append("one lowercase letter")

    print(f"Invalid password. Missing: {', '.join(missing)}. Try again.")



def get_min_length_string(message: str, min_length: int) -> str:
  print(message)

  while True:
    value = input()

    if len(value) >= min_length:
      return value

    print(f"Input must be at least {min_length} characters long. Try again.")
