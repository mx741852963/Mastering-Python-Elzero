# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# Try     => Test The code For Errors
# Except  => handle the errors
# ----------------------------
# Else    => if no errors
# finally => run the code
# ------------------------------------
# number = int(input("Enter Your Age : "))
# print(number)
# print(type(number))
# try:  # try the code and test errors
#     number = int(input("Enter Your Age : "))
#     print("This Will Print Because NO Error from try")
# except:  # handel the errors if its found
#     print("This Will Not Print Because The Error")
# else:  # if there is no error
#     print("This Will Print Because NO Error from else")
# finally:  # will run any way
#     print("This Will Print any way")


# print(int("hello"))
try:
    # print(10 / 0)
    # print(x)
    print(int("hello"))
except ZeroDivisionError:
    print("Cant Divide by Zero")
except NameError:
    print("identifier not found")
except ValueError:
    print("ValueError bla bla")
except:
    print("Something else")
