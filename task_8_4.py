# Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так,
# например:
# def val_checker...
#   ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#   return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
# ...
#   raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?
from functools import wraps


def val_checker(my_arg):
    def _val_checker(func):
        @wraps(func)
        def wrapper(number):
            if my_arg(number) > 0:
                result = func(number)
                return result
            else:
                msg = f'wrong val {number}'
                raise ValueError(msg)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5), calc_cube.__name__)
print(calc_cube(-5))
