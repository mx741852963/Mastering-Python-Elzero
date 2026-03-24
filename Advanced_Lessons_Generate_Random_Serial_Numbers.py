# Advanced Lessons – Generate Random Serial Numbers
import string
import random


# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# def make_serial_number(n):
#     return ''.join(random.choice(string.ascii_letters) for _ in range(n))
# print(make_serial_number(10))
# print(make_serial_number(95))
def make_serial_number(n):
    alphabet = string.ascii_letters + string.digits
    print(''.join(random.choice(alphabet) for _ in range(n)))


make_serial_number(10)
# def make_serial_number(count):
#     alphabet = string.ascii_letters + string.digits
#     chars_count = len(alphabet)
#     # print(chars_count) 62
#     serial_number = []
#     while count > 0:
#         random_number = random.randint(0, chars_count - 1)
#         random_char = alphabet[random_number]
#         serial_number.append(random_char)
#         count = count - 1
#     return print(''.join(serial_number))
#
#
# make_serial_number(10)
