import utils


class User:
    @staticmethod
    def register_user():
        print("\n===== USER REGISTRATION =====")

        user_id = utils.get_non_empty_input("Enter User ID: ")
        name = utils.get_non_empty_input("Enter Name: ")
        email = utils.get_non_empty_input("Enter Email: ")
        password = utils.get_non_empty_input("Enter Password: ")
        role = utils.get_non_empty_input("Enter Role (ADMIN/CUSTOMER): ").upper()

        if User.validate_role(role):
            print("Registration successful")
            return [user_id, name, email, password, role]

        print("Invalid role. Enter ADMIN or CUSTOMER.")
        return None

    @staticmethod
    def display_user(user_data):
        if user_data is not None:
            print("\n===== USER DETAILS =====")
            print("User ID:", user_data[0])
            print("Name:", user_data[1])
            print("Email:", user_data[2])
            print("Role:", user_data[4])

    @staticmethod
    def validate_role(role):
        return role in ["ADMIN", "CUSTOMER"]


class Vehicle:
    @staticmethod
    def register_vehicle():
        print("\n===== VEHICLE REGISTRATION =====")

        vehicle_id = utils.get_non_empty_input("Enter Vehicle ID: ")
        owner_id = utils.get_non_empty_input("Enter Owner ID: ")
        model = utils.get_non_empty_input("Enter Vehicle Model: ")
        battery_capacity = utils.get_positive_float("Enter Battery Capacity (kWh): ")
        efficiency = utils.get_positive_float("Enter Energy Efficiency (Wh/km): ")

        print("Vehicle registered successfully")
        return [
            vehicle_id,
            owner_id,
            model,
            battery_capacity,
            efficiency
        ]

    @staticmethod
    def display_vehicle(vehicle_data):
        if vehicle_data is not None:
            print("\n===== VEHICLE DETAILS =====")
            print("Vehicle ID:", vehicle_data[0])
            print("Owner ID:", vehicle_data[1])
            print("Model:", vehicle_data[2])
            print("Battery Capacity:", vehicle_data[3], "kWh")
            print("Efficiency:", vehicle_data[4], "Wh/km")

    @staticmethod
    def calculate_range(battery_capacity, efficiency):
        if battery_capacity > 0 and efficiency > 0:
            return (battery_capacity * 1000) / efficiency
        return 0

    @staticmethod
    def calculate_energy(distance, efficiency):
        if distance >= 0 and efficiency > 0:
            return (distance * efficiency) / 1000
        return 0
