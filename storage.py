import csv
import os
def save_user(user):
    with open("users.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(user)
def load_users():
    users=[]
    with open("users.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            users.append(row)
    return users 
def save_vehicle(vehicle):
    with open("vehicle.csv","a",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(vehicle)
def load_vehicles():
    vehicles=[]
    with open("vehicles.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            vehicles.append(row)
    return vehicles                               