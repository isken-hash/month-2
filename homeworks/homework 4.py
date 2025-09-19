pups = 5
class User:
    total_user = 0


    def __init__(self,name, email,):
        self.name = name
        self.email = email
        self.total_user = 1

    @classmethod
    def get_total_user(cls):
        return cls.total_user

    @staticmethod
    def say_hello():
        if pups == 3:
            print('how are you pups')
        else:
            print('you bad')



user_1 = User('albert',"pupsikov@gmail.pups",)
user_2 = User('nikita',"pups",)

user_1.total_user = 4

print(User.total_user)
print(user_1.total_user)

User.say_hello()


