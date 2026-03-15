import datetime
import pyfiglet


def get_name():
    n = str(input("Enter your name: "))
    print(f"Hello {n}!")
    return n


name = get_name()


def get_time():
    print("Hello Plz Enter Your Birthday")
    y = int(input("Year:"))
    m = int(input("Month:"))
    d = int(input("Day:"))
    return y, m, d


c = False
while not c:
    year, month, day = get_time()

    if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
        birthday = datetime.datetime(year, month, day)
        print(f"Birthday is: {birthday}")
        c = True
    else:
        print("Wrong Time! Try again.")
