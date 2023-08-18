"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ
ยี่ห้อรถ (brand)
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที
"""
class Vehicle:
    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price
        #self.my_vihecle.append(self)

    def Vehicle_info(self):
        print(f'brand:{self.brand}'
              f' model:{self.model}'
              f' color:{self.color}'
              f' maxspeed:{self.maxspeed}'
              f' price:{self.price}')
# vc = []

# v = int(input('How many Vehicle? : '))
# for i in range(v):
#     s = Vehicle()
#     print(f"Please, enter Vehicle info {i+1}:")
#     s.brand = input("Enter brand: ")
#     s.model = input("Enter model: ")
#     s.color = input("Enter color: ")
#     s.maxspeed = input("Enter maxspeed: ")
#     s.price = input("Enter price: ")
#     vc.append(s)
# for i in vc:
#     i.Vehicle_info()