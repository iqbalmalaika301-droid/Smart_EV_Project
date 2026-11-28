
import models

def simulate_trip(vehicle_data, start, destination, distance, battery_percentage):

    # Get vehicle information
    vehicle_id = vehicle_data[0]
    vehicle_model = vehicle_data[2]
    battery_capacity = float(vehicle_data[3])
    efficiency = float(vehicle_data[4])

    # Validate inputs
    if distance <= 0:
        print("Invalid distance!")
        return None

    if battery_percentage <= 0 or battery_percentage > 100:
        print("Invalid battery percentage!")
        return None

    if not start or not destination:
        print("Location cannot be empty!")
        return None

    # Calculate available battery energy
    available_energy = battery_capacity * battery_percentage / 100

    # Calculate energy required for trip
    energy_consumed = (distance * efficiency) / 1000

    # Calculate remaining battery energy
    remaining_energy = available_energy - energy_consumed

    # Calculate maximum possible range
    possible_range = models.calculate_range(
        available_energy, efficiency
    )

    # Display trip details
    print("\n======= EV TRIP SIMULATION =======")

    print("Vehicle ID:", vehicle_id)
    print("Vehicle Model:", vehicle_model)
    print("Starting Location:", start)
    print("Destination:", destination)
    print("Trip Distance:", distance, "km")
    print("Starting Battery:", battery_percentage, "%")
    print("Available Energy:", round(available_energy, 2), "kWh")
    print("Required Energy:", round(energy_consumed, 2), "kWh")
    print("Estimated Range:", round(possible_range, 2), "km")

    # Check battery availability
    if energy_consumed > available_energy:

        print("\nInsufficient Battery!")
        print("Your vehicle cannot complete this trip.")

        return {
            "status": "Failed",
            "vehicle_id": vehicle_id,
            "distance": distance,
            "energy_consumed": energy_consumed
        }

    else:

        # Calculate remaining battery percentage
        remaining_percentage = (
            remaining_energy / battery_capacity
        ) * 100

        print("\nTrip Simulation Successful!")
        print("Energy Consumed:", round(energy_consumed, 2), "kWh")
        print("Remaining Energy:", round(remaining_energy, 2), "kWh")
        print("Remaining Battery:", round(remaining_percentage, 2), "%")

        return {
            "status": "Successful",
            "vehicle_id": vehicle_id,
            "start": start,
            "destination": destination,
            "distance": distance,
            "energy_consumed": energy_consumed,
            "remaining_energy": remaining_energy,
            "remaining_battery": remaining_percentage
        }

def run_trip_simulation(vehicles):

    print("\n======= START EV TRIP =======")

    # Check registered vehicles
    if not vehicles:
        print("No registered vehicles found!")
        return None

    # Display registered vehicles
    print("\nRegistered Vehicles:")

    for vehicle in vehicles:
        print("Vehicle ID:", vehicle[0])
        print("Vehicle Model:", vehicle[2])
        print("----------------------")

    # Select vehicle
    vehicle_id = input("Enter Vehicle ID: ").strip()

    selected_vehicle = None

    for vehicle in vehicles:

        if vehicle[0] == vehicle_id:
            selected_vehicle = vehicle
            break

    if selected_vehicle is None:
        print("Vehicle not found!")
        return None

    # Get trip information
    start = input("Enter Starting Location: ").strip()
    destination = input("Enter Destination: ").strip()

    try:
        distance = float(input("Enter Trip Distance (km): "))

        battery_percentage = float(
            input("Enter Current Battery Percentage: ")
        )

    except ValueError:
        print("Please enter valid numeric values!")
        return None

    # Run trip simulation
    return simulate_trip(
        selected_vehicle,
        start,
        destination,
        distance,
        battery_percentage
    )

    

   
