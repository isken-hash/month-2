
def pupsik(func):
    def wrapper(*args, **kwargs):
        print(f'до вызова {func.__name__}')
        result = func(*args, **kwargs)
        print(f'до вызова {func.__name__}')
        return result
    return wrapper

@pupsik
def hello_world():
    print('hello world')

@pupsik
def add_numbers(num1, num2):
    return num1 * num2

hello_world()
print(add_numbers(9999,9999))


def blahblah():
    print('blahblah')





