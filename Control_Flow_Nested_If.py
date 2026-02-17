# -----------------
# -- Control Flow Nested If --
# ----------------
uName = "osama"
isStudent = "No"
uCountry = "KSA"
cName = "Python Course"
cPrice = 100
# cDiscount = 30
if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

    if isStudent == "Yes":
        print(f"Hello {uName} Because Your Are From {uCountry} And Student ")
        print(f"The Course \"{cName}\" has a price of: ${cPrice - 90}")
    else:
        print(f"Hello {uName} Because Your Are From {uCountry} ")
        print(f"The Course \"{cName}\" has a price of: ${cPrice - 80}")
elif uCountry == "Kuwait" or uCountry == "Bahrain":
    print(f"Hello {uName} Because Your Are From {uCountry} ")
    print(f"The Course \"{cName}\" has a price of: ${cPrice - 50}")
else:
    print(f"Hello {uName} Because Your Are From {uCountry}")
    print(f"The Course \"{cName}\" has a price of: ${cPrice - 30}")
