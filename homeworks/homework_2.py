class Person:
    def __init__(self, name, birth_date,pofi):
         self.name = name
         self.birth_date = birth_date
         self.porofeci = pofi


    def helo(self):
     print(f'меня зовут {self.name} я родился {self.birth_date} я работаю {self.porofeci}')


class Classmate(Person):
    def helo(self):
        print(f'меня зовут {self.name} я однокласник саши я был рожден в {self.birth_date} сейчас работаю {self.porofeci}')

class Friend(Person):
    def helo(self):
        print(f'мое имя {self.name} я друг саши я родился {self.birth_date} на данный момент работаю {self.porofeci}')



friend = Friend('денчик','9,12,1998','кибер безопасностю')
friend1 = Friend('бекжан','10,13,2012', 'строитель')
friend.helo()
friend1.helo()


classmate = Classmate('никита','5,2,1968','учитель')
classmate1 = Classmate('амир','8,2,1987','таксистом')
classmate.helo()
classmate1.helo()




