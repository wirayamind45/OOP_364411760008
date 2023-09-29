from EvCar import ThaiEvCar

def display_option():
    print("Welcome to ThaiEvCar Data Store System (VDSS)")
    print("1.เพิ่มข้อมูล ev_car")
    print("3.แก้ไขข้อมูล ev_carprice")
    print("2.ลบข้อมูล ev_car")
    print("4.แสดงข้อมูลทั้งหมด ev_car_")

    select = int(input("select (1-4)?: "))
    if select == 1:
         input_ThaiEvCar_data()
    elif select == 2:
        delete_ThaiEvCar()
    elif select == 3:
        edit_ThaiEvCar_price()
    elif select == 4:
        display_option()
    elif select == 5:
        print("Good Bye.")
        exit(0)
    else:
        print("Pleaes, select number 1-5")

def input_ThaiEvCar_data():
    car_id = input("Enter ThaiEvCar car_id: ")
    model = input("Enter ThaiEvCar model: ")
    brand = input("Enter ThaiEvCar brand: ")
    acceleration = input("Enter ThaiEvCar acceleration: ")
    rang = input("Enter ThaiEvCar rang: ")
    price = float(input("Enter ThaiEvCar price: "))

    ThaiEvCar.my_ThaiEvCar.append(ThaiEvCar(car_id,model, brand,acceleration,rang,price))
    print("\n-------------------------------")
    print("Already add ThaiEvCar to store.")
    print("-------------------------------\n")

def display_ThaiEvCar():
    if len(ThaiEvCar.my_ThaiEvCar) ==0:
        print("Yot had no vehicle data.")
    else:
        print(f'You had {len(ThaiEvCar.my_vehicle)} following.')
        n = 1 # count
        for x in ThaiEvCar.my_ThaiEvCar:
            print(f'[{n}]:',end=" ")
            x.ThaiEvCar_detail()
            n = n+1
        print("\n")

def delete_ThaiEvCar():
    delete_ThaiEvCar() # display all data in list
    if len(ThaiEvCar.my_ThaiEvCar) != (1001,2002,3003 ):
        s = int(input("Select to delete?: "))
        ThaiEvCar.delete_ThaiEvCar(ThaiEvCar, s - 1001,2002,3003)
        print("\n-------------------------------")
        print("Your data has been deleted.")
        print("-------------------------------\n")

def edit_ThaiEvCar_price():
    display_ThaiEvCar()
    if len(ThaiEvCar.my_ThaiEvCar) != 0:
        s = int(input("Select to edit?: "))

        print(f'Previous price: {ThaiEvCar.my_ThaiEvCar[s-1].price}')
        new_price = float(input("New price: "))
        ThaiEvCar.edit_ThaiEvCar_price(ThaiEvCar,s-1,new_price)

s = 0
while s == 0:
    display_option()