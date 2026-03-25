# -------------------------
# -- Break Continue Pass --
# -------------------------
myNumbers = [1, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 17, 18, 20]
# Continue
for number in myNumbers:
    if number == 13:
        continue
    print(number)
print("=" * 40)
# Break
for number in myNumbers:
    if number == 13:
        break
    print(number)
print("=" * 40)
# Pass
for number in myNumbers:
    if number == 13:
        pass
    print(number)
print("=" * 40)
