# ---------------------------
# -- Loop While Training   --
# -- Simple Password Guess --
# ---------------------------

tries = 4
mainPassword = "Ahmad@123"
inputPassword = input("Enter your password: ")
while inputPassword != mainPassword:
    tries -= 1
    print(f"Wrong password. Try again {'Last' if tries == 1 else tries} left")
    inputPassword = input("Enter your password: ")
    if tries == 1:
        # print("Your chance done ")
        break

print("Password is correct " if inputPassword == mainPassword else "Password is incorrect")
