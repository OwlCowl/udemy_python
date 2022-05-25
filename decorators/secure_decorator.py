import functools


user = {'username': 'Jose', 'useright': 'admin'}

def user_has_persmission(func):
    #wrap function and save doc string, name specify for diff funcs
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('useright') == 'admin':
            return func(*args, **kwargs)
    return secure_func

@user_has_persmission
def my_func(panel):
    return f'Passwords for {panel} is 123'

@user_has_persmission
def another():
    pass


print(my_func('panel'))
print(another())

