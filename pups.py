class cat:
    def __init__(self, name, height, age,):
        self.name = name
        self.height = height
        self.age = age


while True:
    jony = input('print name')
    lelop = input('print age')
    pelmen = input('print height')

    lelop = int(lelop)
    pelmen = int(pelmen)

    pupsik = cat(jony, pelmen, lelop)

    print(f'Кота зовут {jony}')
    print(f'Возраст кота: {lelop}')
    print(f'Рост кота: {pelmen}')




