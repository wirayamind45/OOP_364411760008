from EvCar import ThaiEvCar

# e = ThaiEvCar(1001,"Tesla","Model 3",6.1,347,559,1759000)

# #display data by using getter
# print(e.get_id(),e.get_brand(),e.get_model())
#
# e.ev_car_detail()
#
# e.set_price(1650000)
# e.ev_car_detail()


# option
def display_option():
    print("Welcome to ThaiEvCar ")
    print("1.Add ThaiEvCar")
    print("2.Display all ThaiEvCar")
    print("3.exit")
    select = int(input("select(1-3) ? : "))
    if select == 1:
        input_ThaiEvCar_data()
    elif select== 2:
        delete_ThaiEvCar()
    elif select == 3:
        print("Good Bye.")
        exit(0)

        print("Please,select number 1-3.")

    # add data
def input_ThaiEvCar_data():
        id = input("Enter ThaiEvCar id: ")
        brand = input("Enter ThaiEvCar brand: ")
        model = input("Enter ThaiEvCar model: ")
        acc_rate = int(input("Enter ThaiEvCar acc_rate: "))
        hp = int(input("Enter ThaiEvCar hp: "))
        range = int(input("Enter ThaiEvCar range: "))
        price = float(input("Enter ThaiEvCar price: "))

        ThaiEvCar.my_ThaiEvCar.append(ThaiEvCar(id,brand,model,acc_rate,hp,range,price))
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

# display data
def display_ThaiEvCar():
    if len(ThaiEvCar.my_ThaiEvCar) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had {len(ThaiEvCar.my_ThaiEvCar)} following:')
        n = 1 #count
        for x in  ThaiEvCar.my_ThaiEvCar:
            print(f'[{n}]:',end="")
            x.ev_car_detail()
            n = n+1
            print("\n")

#delete vehicle
def delete_ThaiEvCar():
    #display all data in list
    display_ThaiEvCar()
    if len(ThaiEvCar.my_ThaiEvCar) == 0:
        print("You had no data to dalete.")
        s = int(input("Select to delete ?: "))

        ThaiEvCar.delete_ThaiEvCar(ThaiEvCar, s-1)
        ThaiEvCar.delete_ThaiEvCar(s-1)
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

# edit vehicle price
def edit_ThaiEvCar_price():
    display_ThaiEvCar()
    if len(ThaiEvCar.my_ThaiEvCar) != 0:
        s = int(input("Select to edit ?: "))
        #display previous price
        print(f'previous price: {ThaiEvCar.my_ThaiEvCar[s-1].price}')
        new_price = input("new price: ")
        ThaiEvCar.edit_ThaiEvCar_price(ThaiEvCar,s-1,new_price)
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

       # run
#my_vehicle = []
s = 0
while s == 0:
    display_option()



