# --------------------------
# -- Date And Time Format --
# --------------------------
# "https://strftime.org/"
# --------------------------
import datetime

myBirthday = datetime.datetime(1999, 12, 31)
print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))
# print(dir(datetime.datetime))
print(myBirthday.strftime("%d %B %Y "))
