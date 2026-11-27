from models import User, Vehicle
import utils
import storage

users = storage.load_users()
vehicles = storage.load_vehicles()

print("Smart EV Charging, Billing and Demand Prediction System")

while True:
    print("\n===== MAIN MENU =====")
    print("1. Login")
    print("2. Register User")
    print("3. Register EV")
    print("4. Simulate Trips")
    print("5. Charging History")
    print("6. Generate Bill")
    print("7. View Chart")
    print("8. Predict Energy Demand")
    print("9. Exit")

    user_selection = utils.get_menu_choice()

    if user_selection == 1:
        print("Login started")

    elif user_selection == 2:
        user_data = User.register_user()

        if user_data is not None:
            users.append(user_data)
            storage.save_user(user_data)
            User.display_user(user_data)

    elif user_selection == 3:
        vehicle_data = Vehicle.register_vehicle()

        if vehicle_data is not None:
            vehicles.append(vehicle_data)
            storage.save_vehicle(vehicle_data)
            Vehicle.display_vehicle(vehicle_data)

    elif user_selection == 4:
        print("EV trip simulation initiated")

    elif user_selection == 5:
        print("Displaying charging history")

    elif user_selection == 6:
        print("Calculating electricity bills")

    elif user_selection == 7:
        print("Visualization section")

    elif user_selection == 8:
        print("Calculating energy usage")

    elif user_selection == 9:
        print("Exiting the system")
        break

    elif user_selection is not None:
        print("Please enter a number from 1 to 9.")
