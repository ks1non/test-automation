# def summerize(a: str, b: int):
#     return a + b
#
#
# summerize(1, 5)

# class Car:
#     def __init__(self, car_name):
#         self.car_name = car_name
#
#     def create_new_car(self):
#         print(f'new car created:{self.car_name}')
#
#
# Car('BMW').create_new_car()


# a = [1, 2]
# print(a)
# a.
# b = Car('BMW')
# b.
#
# BASEURL = 'www.google.com'

# """1. принимает на вход 1 параметр
#    2. проверяем валидно ли значение
#    3. проверяем валидность (только целые число 0 - 10 )"""
#
#
# def validatin(a):
#     if 0 <= a <= 10 and isinstance(a, int):
#         print('valid')
#     elif not isinstance(a, int) and a > 0:
#         print(f'{a} is not int')
#     elif a < 0:
#         print(f"{a} is negative number")
#     else:
#         print(f'{a} out of range')
#
#
# validatin(-1.5)
# validatin(2.5)
# validatin(0)
# validatin(1)
# validatin(9)
# validatin(10)
# validatin(11)
