# --------------
# -- Control Flow --
# -- If,Elif,Else --
# -- Make Decisions --
# --------------
uName = "osama"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100
# cDiscount = 30
if uCountry == "Egypt":
    print(f"Hello {uName} Because Your Are From {uCountry} ")
    print(f"The Course \"{cName}\" has a price of: ${cPrice - 80}")
elif uCountry == "KSA":
    print(f"Hello {uName} Because Your Are From {uCountry} ")
    print(f"The Course \"{cName}\" has a price of: ${cPrice - 60}")
elif uCountry == "Kuwait":
    print(f"Hello {uName} Because Your Are From {uCountry} ")
    print(f"The Course \"{cName}\" has a price of: ${cPrice - 50}")
else:
    print(f"Hello {uName} Because Your Are From {uCountry}")
    print(f"The Course \"{cName}\" has a price of: ${cPrice - 30}")
