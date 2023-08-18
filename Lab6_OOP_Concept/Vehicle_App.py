from Vehicle import Vehicle

# option
def display_option():
    print("Welcom to vehicle Data Store  System (VDSS)")
    print("1.Add Vehicle")
    print("2.Display all Vehicle")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_option()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")
#add data
def input_vehicle_data():
    brand = input("Enter vehicle brand: ")
    modal = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = int(input("Enter vehicle max sprrd:"))
    price = float(input("Enter vehicle  price: "))

    my_vehicle.append(Vehicle(brand,modal,color,maxspeed,price))
    print("\n------------------------------------")
    print("Already add vehicle to store. ")
    print("------------------------------------\n")

#displaydata
def display_Vehicle():
    if len(my_vehicle) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had {len(my_vehicle)} following:')
        for x in my_vehicle:
            x.vehicle_detail()
        print("\n")


#run
my_vehicle = []
s = 0
while s == 0:
    display_option()