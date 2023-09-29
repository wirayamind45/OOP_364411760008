from Vehicle import vehicle


# option เพิ่มข้อมูล
def display_option():
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("\n-------------------------------")
    print("1.Add Vehicle")
    print("2.Display all vehicle")
    print("3.Delete Vehicle")
    print("4.Edit Vehicle Price")
    print("5.Edit Vehicle Color")
    print("6.exit")
    print("-------------------------------\n")
    select = int(input("select (1-5)?: "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        delete_vehicle()
    elif select == 4:
        edit_vehicle_price()
    elif select == 5:
        edit_vehicle_color()
    elif select == 6:
        print("Good Bye.")
        exit(0)
    else:
        print("Pleaes, select number 1-5")


# Add Data เพิ่มข้อมูล
def input_vehicle_data():
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = input("Enter vehicle maxspeed: ")
    price = float(input("Enter vehicle price: "))


    vehicle.my_vehicle.append(vehicle(brand,model,color,maxspeed,price))
    print("\n-------------------------------")
    print("Already add vehicle to store.")
    print("-------------------------------\n")


# Display data
def display_vehicle():
    if len(vehicle.my_vehicle) ==0:
        print("Yot had no vehicle data.")
    else:
        print(f'You had {len(vehicle.my_vehicle)} following.')
        n = 1 # count
        for x in vehicle.my_vehicle:
            print(f'[{n}]:',end=" ")
            x.vehicle_detail()
            n = n+1
        print("\n")


# delete vehicle ลบ
def delete_vehicle():
    display_vehicle() # display all data in list
    if len(vehicle.my_vehicle) != 0:
        s = int(input("Select to delete?: "))

        vehicle.delete_vehicle(vehicle, s-1)
        print("\n-------------------------------")
        print("Your data has been deleted.")
        print("-------------------------------\n")


# edit vehicle price แก้ไข
def edit_vehicle_price():
    display_vehicle()
    if len(vehicle.my_vehicle) != 0:
        s = int(input("Select to edit?: "))

        print(f'Previous price: {vehicle.my_vehicle[s-1].price}')
        new_price = float(input("New price: "))
        vehicle.edit_vehicle_price(vehicle,s-1,new_price)

def edit_vehicle_color():
    display_vehicle()
    if len(vehicle.my_vehicle) != 0:
        s = int(input("Select to edit?: "))

        print(f'Previous color: {vehicle.my_vehicle[s-1].color}')
        new_color = input("New Color: ")
        vehicle.edit_vehicle_color(vehicle,s-1,new_color)


# my_vehicle = []
s = 0
while s == 0:
    display_option()