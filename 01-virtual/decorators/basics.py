from functools import wraps

def my_decorators(func):

    @wraps(func)
    def wrapper():
        print('Before func run')
        func()
        print('After func run')
    return wrapper


@my_decorators
def greet():
    print('Hello from decorators')

greet()