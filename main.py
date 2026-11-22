#Displaying project title
print("Smart_EV_Project")
#Starting the loop that keeps the program running 
while True:
    print("\n===== MAIN MENU=====")
    print("1. Login")
    print("2. Register User")
    print("3. Register EV")
    print("4. Simulate Trips")
    print("5. Charging History")
    print("6. Generate Bill")
    print("7. View Chart ")
    print("8. Predict Energy Demand")
    print("9. Exit")

    #Ask the user to select an option
    user_selection= input("Enter your option:")
    
    #Check which option the user selected
    
    if user_selection == "1":
        print("Login started")

    elif user_selection == "2":
        print("User registration initiated")
    elif user_selection == "3":
        print("Electric vehicle registration initiated")
    elif user_selection == "4":
        print("EV trip simulation initiated")
    elif user_selection == "5":
        print("Displaying charging history")
    elif user_selection == "6":
        print("Calculating electricity bills")
    elif user_selection == "7":
        print("Visualization section")
    elif user_selection == "8":
        print("Calculating energy usage")
    elif user_selection == "9":
        print("Exit the system")
        break

    else:
        print("Please enter a correct number from the menu")


    



    
