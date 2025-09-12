class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.__speed = 0  # Приватный атрибут

    def accelerate(self, acc):
        # setter
        if self.__speed + acc > self.max_speed:
            raise ValueError("Скорость не может быть больше максимальной")
        else:
            self.__speed += acc

    def get_speed(self):
        # getter
        return self.__speedgit branch

