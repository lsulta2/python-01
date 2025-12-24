from functools import wraps

def require_admin(func):
    @wraps(func)

    def wrapper(user_role): 

        if user_role != 'admin':
            print("Access denied: Admin only")
            return None
        else:
                return func(user_role)

    return wrapper


@require_admin
def inventory_access(role):
    print('Access granted to inventory')


inventory_access('admin')
inventory_access('user')


