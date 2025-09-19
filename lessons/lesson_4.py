from urllib.request import AbstractBasicAuthHandler


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__fined = False


    def drive__to_location(self, location):
        print(f'my car {self.model} driving to {location}')

kaka1 = input('напишите бренд')
kaka = input('напишите модель')



pupsik = Car(kaka1, kaka)
pupsik.drive__to_location('дом')
del pupsik





