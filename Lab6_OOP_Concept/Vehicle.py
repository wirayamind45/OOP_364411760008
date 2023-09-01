
# class attribute
class vehicle:
    my_vehicle = []

    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price


# display object atteibute
    def vehicle_detail(self):
        print(f'brand:{self.brand} '
              f'model:{self.model} '
              f'color:{self.color} '
              f'maxspeed:{self.maxspeed} '
              f'price:{self.price}')

    def delete_vehicle(self,index):
        self.my_vehicle.pop(index)

    def edit_vehicle_price(self,index,new_price):     # edit vehicle
        self.my_vehicle[index].price = new_price

    def edit_vehicle_color(self,index,new_color):
        self.my_vehicle[index].color = new_color


#std = []
#n = int(input('How many Vehicle : '))
#for i in range(n):
#    s = Vehicle()
#    print(f"please, Enter brand info:")
#    s.brand = input("Enter brand:")
#    s.model = input("Enter model:")
#    s.color = input("Enter color:")
#    s.maxspeed = input("Enter maxspeed:")
#    s.price = input("Enter price:")
#    std.append(s)

#for i in std:
#    i.Vehicle_info()