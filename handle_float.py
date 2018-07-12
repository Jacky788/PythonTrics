from decimal import *

x = 7 / 3
print('x is {}'.format(x))
print(type(x))  # python 3

x = 7 // 3
print('x is {}'.format(x))
print(type(x))  # python 3

x = 0.1 + 0.1 + 0.1 - 0.3
print('x is {}'.format(x))
print(type(x))  # floating point value is not good with money

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))  # use someting like Decimal instead when working with money