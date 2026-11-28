import csv
import os

USER_FILE = "users.csv"
VEHICLE_FILE = "vehicles.csv"

USER_HEADERS = ["User ID", "Name", "Email", "Password", "Role"]
VEHICLE_HEADERS = [
    "Vehicle ID",
    "Owner ID",
    "Model",
    "Battery Capacity (kWh)",
    "Efficiency (Wh/km)"
]


def create_file(file_name, headers):
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


def save_user(user_data):
    create_file(USER_FILE, USER_HEADERS)

    with open(USER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(user_data)


def save_vehicle(vehicle_data):
    create_file(VEHICLE_FILE, VEHICLE_HEADERS)

    with open(VEHICLE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(vehicle_data)


def load_users():
    create_file(USER_FILE, USER_HEADERS)

    with open(USER_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        return [row for row in reader]


def load_vehicles():
    create_file(VEHICLE_FILE, VEHICLE_HEADERS)

    with open(VEHICLE_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        vehicles = []

        for row in reader:
            if row:
                row[3] = float(row[3])
                row[4] = float(row[4])
                vehicles.append(row)

        return vehicles
