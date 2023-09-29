class ThaiEvCar :
    my_ThaiEvCar = []

    def __init__(self,id,brand,model,acc_rate,hp,range,price):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__acc_rate = acc_rate
        self.__hp = hp
        self.__range = range
        self.__price = price

    def ev_car_detail (self):
        print(f'ID : {self.__id}'
              f'Brand: {self.__brand}'
              f'Model : {self.__model}'
              f'Acceleration : {self.__acc_rate}'
              f'HP :{self.__hp}'
              f'Range : {self.__range}'
              f'Price : {self.__price}')

#getter and setter methods
    def get_id(self):
        return self.__id
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_acc_rate(self):
        return self.__acc_rate
    def get_hp(self):
        return  self.__hp
    def get_range(self):
        return self.__range
    def get_price(self):
        return self.__price



    def set_brand(self,brand):
        self.__brand = brand
    def set_model(self,model):
        self.__model = model
    def set_acc_rate(self,acc_rate):
        self.__acc_rate = acc_rate
    def set_acc_hp(self,hp):
        self.__hp = hp
    def set_range(self,range):
        self.__range = range
    def set_price(self,price):
        self.__price = price






