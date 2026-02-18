# ---------------
# -- Calculate Age Advanced Version --
# --------------
# Collect Age Data

age = int(input("What\'s your Age?").strip())
# Collect Time Unit Data
unit = str(input("What\'s your Unit? : \n months ?\n weeks ?\n days ?\n hours ?\n minutes ?\n seconds ?\n").strip())
if unit == "months":
    age = age * 12
elif unit == "weeks":
    age = age * 4 * 12
elif unit == "days":
    age = age * 365
elif unit == "hours":
    age = age * 24 * 365
elif unit == "minutes":
    age = age * 60 * 365 * 24
elif unit == "seconds":
    age = age * 60 * 365 * 24 * 60
else:
    print("Please enter a valid unit")
print(f"your age is {age:,} {unit} old")
