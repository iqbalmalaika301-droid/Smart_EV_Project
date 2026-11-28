import utils


class User:
    def generate_next_user_id(existing_users):
        if not existing_users:
            return "0001"

        max_id = 0
        for user in existing_users:
            if user and str(user[0]).isdigit():
                user_num = int(user[0])
                if user_num > max_id:
                    max_id = user_num

        next_id = max(max_id + 1, len(existing_users) + 1)
        return f"{next_id:04d}"

    def register_user(existing_users):
        print("\n===== USER REGISTRATION =====")

        name = utils.get_non_empty_input("Enter Name: ")
        email = utils.get_valid_email("Enter Email: ")
        password = utils.prompt_valid_password("Enter Password: ")
        role = utils.get_non_empty_input("Enter Role (ADMIN/CUSTOMER): ").upper()

        if not User.validate_role(role):
            print("Invalid role. Enter ADMIN or CUSTOMER.")
            return None

        user_id = User.generate_next_user_id(existing_users)
        print("Registration successful")
        return [user_id, name, email, password, role]

    def display_user(user_data):
        if user_data is not None:
            print("\n===== USER DETAILS =====")
            print("User ID:", user_data[0])
            print("Name:", user_data[1])
            print("Email:", user_data[2])
            print("Role:", user_data[4])

    def validate_role(role):
        return role in ["ADMIN", "CUSTOMER"]


class Vehicle:
    def register_vehicle():
        print("\n===== VEHICLE REGISTRATION =====")

        vehicle_id = utils.get_non_empty_input("Enter Vehicle ID: ")
        owner_id = utils.get_non_empty_input("Enter Owner ID: ")
        model = utils.get_min_length_string("Enter Vehicle Model: ", 5)
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

    def display_vehicle(vehicle_data):
        if vehicle_data is not None:
            print("\n===== VEHICLE DETAILS =====")
            print("Vehicle ID:", vehicle_data[0])
            print("Owner ID:", vehicle_data[1])
            print("Model:", vehicle_data[2])
            print("Battery Capacity:", vehicle_data[3], "kWh")
            print("Efficiency:", vehicle_data[4], "Wh/km")

    def calculate_range(battery_capacity, efficiency):
        if battery_capacity > 0 and efficiency > 0:
            return (battery_capacity * 1000) / efficiency
        return 0

    # Added battery_capacity parameter and fixed 'efficiency' spelling
    def calculate_energy(battery_used, battery_capacity, efficiency):
        if battery_used > 0 and battery_capacity > 0 and efficiency > 0:
            return (battery_used / 100) * (battery_capacity * (efficiency / 100))
        return 0
