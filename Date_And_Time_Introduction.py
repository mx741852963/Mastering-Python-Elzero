# --------------------------------
# -- Date And Time Introduction --
# --------------------------------
import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))
# Print The Current Date And Time
print(datetime.datetime.now())
print("*" * 50)
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)
print("*" * 50)
# Print Start And End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)
# Print The Current Time
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)
print(datetime.datetime.now().microsecond)
print("*" * 50)
print(datetime.time.min)
print(datetime.time.max)
print("*" * 50)
# Print Specific Date
print(datetime.datetime(1999, 12, 29))
print(datetime.datetime(1999, 12, 29, 10, 10, 10))
print("*" * 50)
myBirthday = datetime.datetime(1999, 10, 20)
dateNow = datetime.datetime.now()
print(dateNow - myBirthday)
print((dateNow - myBirthday).days)
