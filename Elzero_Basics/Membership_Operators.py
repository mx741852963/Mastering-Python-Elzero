# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String
name = "ahmad"
print("a" in name)
print("h" in name)
print("A" in name)
print("=" * 50)
friends = ["ahmad", "ali", "karem"]
print("ahmad" in friends)
print("ali" in friends)
print("sayed" not in friends)
print("=" * 50)
# Using In and Not In With Condition
countriesOne = ["Egypt", "Ghana", "Mumbai", "Syria"]
countriesOneDiscount = 80
countriesTwo = ["KSA", "UK", "USA"]
countriesTwoDiscount = 50
myCountry = "Syria"
if myCountry in countriesOne:
    print(f"Country is  {myCountry} and {countriesOneDiscount} Discount")
elif myCountry in countriesTwo:
    print(f"Country is  {myCountry} and {countriesTwoDiscount} Discount")
else:
    print("your country is not in the list")
