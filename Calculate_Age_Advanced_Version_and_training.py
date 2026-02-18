# ---------------
# -- Calculate Age Advanced Version And Training --
# Write note
print("#" * 100)
print("You Can write the first letter of full name of the time unit".title().center(100, "#"))
print("#" * 100)
# Collect Age Data
age = int(input("What\'s your Age? ").strip())
# Collect Time Unit Data
unit = str(input("What\'s your Unit? : \n months ?\n weeks ?\n days ?\n").strip().lower())
# Get Time Uint Data
months = age * 12
weeks = months * 4
days = age * 365
if unit == "months" or unit == "m":
    print("You chose the unit for a month ")
    print(f"you lived for  {months:,} Months")
elif unit == "weeks" or unit == "w":
    print("You chose the unit for a week ")
    print(f"you lived for  {weeks:,} Weeks")
elif unit == "days" or unit == "d":
    print("You chose the unit for a day ")
    print(f"you lived for  {days:,} Days")
