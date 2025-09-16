class Car:
    # инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f"Car {self.model} is drinig to {location}")

car_honda = Car("silver", "Honda")
print(car_honda)

car_subaru = Car("black", "Subaru")
print(car_subaru)




