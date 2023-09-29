class ThaiEvCar:
    my_ThaiEvCar = []

    def __init__(self,car_id,model,brand,acceleration,hp,range,price):
        self.car_id = car_id
        self.model = model
        self.brand = brand
        self.acceleration = acceleration
        self.hp = hp
        self.range = range
        self.price = price

    def ThaiEvCar_detail(self):
        print(f'car_id:{self.car_id} '
              f'model:{self.model} '
              f'brand:{self.brand} '
              f'acceleration:{self.acceleration} '
              f'hp:{self.hp}'
              f'range:{self.range}'
              f'price:{self.price}')

    def delete_ThaiEvCar (self, index):
            self.my_ThaiEvCar.pop(index)

    def edit_ev_car_price(self, index, new_price):  # edit vehicle
            self.my_ThaiEvCar[index].price = new_price
