# ------------------------------------
# -- Practical Membership Control --
# ------------------------------------
# List Contains Admin
admins = ["Ahmad", "Ali", "Karm", "Manal", "Osama"]
# Login
name = input("What is your name? ").strip().capitalize()
if name in admins:
    print(f"Hello {name}, welcome Back You are an administrator.")
    option = input("Delete Or update your Name  ? ").strip().capitalize()
    # Update Option
    if option == "Update":
        theNewName = input("What is your new name? ").strip().capitalize()
        # admins.remove(name)
        # admins.append(theNewName)
        admins[admins.index(name)] = theNewName
        print("Name Updated")
    # Delete Option
    elif option == "Delete":
        admins.remove(name)
        print("Name Deleted")
        print(admins)
    # Wrong Option
    else:
        print("Wrong Input")
else:
    status = input("Do you want to add you ? Y or N ").capitalize()
    if status == "Y":
        name = input("What is your name? ").strip().capitalize()
        admins.append(name)
        print("Name Added")
        print(admins)
    elif status == "N":
        print("Name Not Added")
        print(admins)
    else:
        print("Wrong Input")
