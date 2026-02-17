# ------------------------------------
#  -- Ternary Conditional Operator --
# -----------------------------------
# country = "Syria"
# if country == "Syria":print(f"The Weather in {country} is 15")
# elif country == "KSA":print(f"The Weather in {country} is 30")
# else:print(f"Country is not in the list".title())
# True !
country = "Syria"
if country == "Syria":
    print(f"The Weather in {country} is 15")
elif country == "KSA":
    print(f"The Weather in {country} is 30")
else:
    print(f"Country is not in the list".title())
# Short IF
movieRate = 18
age = 16
if age < movieRate:
    print(f"Age is less than {movieRate}")  # Condition if True
elif age > movieRate:
    print(f"Age is greater than {movieRate}")  # Condition if False
print(f"Age is less than {movieRate}" if age < movieRate else f"Age is greater than {movieRate}")
# Condition if True | If Condition | Else | Condition if False
