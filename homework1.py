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


class Person:
    def __init__(self, name, birth_date, profession, higher_education, occupation):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession
        self.__higher_education = higher_education
        self.__occupation = occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def occupation(self):
        return self.__occupation


class Classmate(Person):
    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f'Меня зовут {self.name}, я одноклассник Саши Я был рожден в {self.birth_date}, сейчас работаю {self.profession}, увлекаюсь {self.occupation}. {edu_text}.')


class Friend(Person):
    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f'Мое имя {self.name}, я друг Саши Я родился {self.birth_date}, на данный момент работаю {self.profession}, мое хобби — {self.occupation}. {edu_text}.')



friend = Friend('Денчик', '9.12.1998', 'специалистом по кибербезопасности', False, 'борьбой')
friend1 = Friend('Бекжан', '13.10.2012', 'строителем', True, 'шахматами')

friend.introduce()
friend1.introduce()

classmate = Classmate('Никита', '2.5.1968', 'учителем', True, 'английским')
classmate1 = Classmate('Амир', '2.8.1987', 'таксистом', True, 'боксом')

classmate.introduce()
classmate1.introduce()


