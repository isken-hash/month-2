class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        log = "высшее оброзования True" if self.higher_education else "высшее оброзования False"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}. "
              f"Моя профессия - {self.occupation}, и у меня - {log}.")

lolo = Person("brat", "04.04.2001", "инженер", True)
lolo2 = Person("pupsik", "02.12.2002", "учитель",  True)
lolo3 = Person("sasa", "12.12.2000", "борец", False)



lolo.introduce()
lolo2.introduce()
lolo3.introduce()


