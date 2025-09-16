class Money:
    def __init__(self, amout=0):
        self.amout = amout

    def __str__(self):
        return f'ezlmplayar money: {self.amout}'

    def __add__(self, other):
        return Money(self.amout + other.amout)

    def __sub__(self, other):
        pass

igor_money = Money(100)
print(igor_money)
adilet_money = Money(250)
total_money = adilet_money + igor_money
print(total_money)