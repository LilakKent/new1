from typing import Callable
import functools


# print(print)
# print(id(print))
# print(type(print))
#
# print('*' * 50)
# not_print = print
# print(not_print)
# print(id(not_print))
#
# not_print(66666666666)


def foo(foo_argument='Vova'):
    """I print many 5-s"""
    print('kEY  55555555555')
    print(f'from foo {foo_argument=}')


#
# #
# # print(foo)
# # foo
# # foo.age = 55533
# # print(foo.age)
# #
# # print(foo.__dict__)
# # print(foo.__name__)
# # print(foo.__doc__)
# # foo()
#
# def func_eater(another_function: Callable):
#     another_function()
#
# func_eater(       foo        )


ff = 'gggggggggg'
n = 666611111


def add_log(func):
    def wrapper(argument):
        print(f'{argument=}')
        n = 10
        print(n)
        print(func, 55555555555511111111111)
        func(argument)
        print(ff, 55555555555511111111111)

    return wrapper


# print(foo)
# print(
#     add_log(foo)
# )
# add_log(foo)('ddddddd')

#
# foo = add_log(foo)
#
# print(foo, 8888888)
#
# foo('I am coming')


def decorate_as_float(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # print(args)
        # print(*args)
        # print(kwargs)
        result = func(*args, **kwargs)
        result = float(result)
        return result
    # wrapper.__dict__ = func.__dict__
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


def auth(func):
    """allow to proceed only for admins"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        name = input('Enter your name: ')
        password = input('Enter your password: ')
        if name == 'admin' and password == '1234':
            result = func(*args, **kwargs)
            return result
        print('Access not allowed')

    return wrapper


@auth
@decorate_as_float
def mul_two_args(value1: int, value2: int) -> int:
    return value1 * value2


@decorate_as_float
def convert_to_int(value: str) -> int:
    """some docstring"""
    if value.isdigit():
        return int(value)
    return 0


res = mul_two_args(5, value2=10)
print(res)

res3 = mul_two_args(5, value2=5888)
print(res3)

res2 = convert_to_int('555')
print(res2)

print(mul_two_args)
print(convert_to_int.__doc__)