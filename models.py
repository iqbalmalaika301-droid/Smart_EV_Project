class User:
    #Register user
    def register_user():
        print("\n ====USER REGISTRATION====")
        user_id = input("ENTER USER ID:")
        name = input("ENTER NAME:")
        email = input("ENTER EMAIL:")
        password = input("ENTER PASSWORD:")
        role = input("ENTER  ROLE(ADMIN/CUSTOMER)")
        if role == "ADMIN" or role == "CUSTOMER": 
            print("Registration successful")

            return[user_id, name, email, password, role]
        

        else:
            print("Invalid role")

            return None
    #Displaying USER Information
    def display_user(user_data):
        if user_data is not None:
            print("\n====USER DETAILS====")
            print("user ID:",user_data[0])
            print("Name:",user_data[1])
            print("Email:",user_data[2])
            print("Role:",user_data[4])
    #Validate user role
    def validate_role(role):
        if role == "ADMIN" or role == "CUSTOMER":
            return True
        else:
            return False

#VEHICLE MANAGEMENT

class Vehicle:
    #Register a new electric vehicle
    def register_vehicle():
        print("\n ====VEHICLE REGISTRATION====")

        vehicle_id = input("Enter Vehicle ID")
        owner_id = input("Enter Owner ID")
        model = input("Enter Vehicle Model:")
        battery_capacity = float(input("Enter Battery Capacity"))
        efficiency = float(input("Enter Energy Efficiency"))

        if battery_capacity > 0 and efficiency > 0:
            print("Vehicle Registered Successfully")
            return [vehicle_id, owner_id, model, battery_capacity, efficiency]
        else:
            print("Invalid battery capacity or effieciency")
            return None
    # Display Vehicle Information
    def display_vehicle(vehicle_data):
        if vehicle_data is not None:
            print("\n ====VEHICLE DETAILS====")
            print("Vehicle ID:", vehicle_data[0])
            print("Owner ID:", vehicle_data[1])
            print("Model:",vehicle_data[2])
            print("Battery Capacity:",vehicle_data[3],"kWh")
            print("Efficiency:",vehicle_data[4],"Wh/km")

    # Calculate estimated driving range
    def calculate_range(battery_capacity,efficiency):
        if battery_capacity > 0 and efficiency >0:

            driving_range = (battery_capacity*1000)/efficiency
            return driving_range
        else:
            return 0 
    # Calculate energy consumed during a trip        
    def calculate_energy(distance,efficiency):
        if distance >=0 and efficiency >0:
            energy = (distance * efficiency)/1000
            return energy
        else:
            return 0
    


    

 