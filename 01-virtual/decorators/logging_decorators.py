
from functools import wraps

def logging_activities(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        print(f'Calling: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Finished: {func.__name__}')
        return result

    return wrapper



@logging_activities

def brew_chai(type, milk = 'no'):
    print(f'Brewing {type} and milk status {milk}')

brew_chai('Lemon')

