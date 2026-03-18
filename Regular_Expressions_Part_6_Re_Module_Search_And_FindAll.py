# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------
import re

# my_string = re.search(r"[A-Z]{2}", "AHmad_ALjmal")
# print(my_string)
# # print(dir(my_string))
# print(my_string.span())
# print(my_string.string)
# print(my_string.group())
# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "ahmad@gf.com")
# if is_email:
#     print("This is an email")
# else:
#     print("This is not an email")
email_input = input("Enter your email address: ")
search_1 = re.findall(r"[A-Za-z0-9.]+@[A-Za-z0-9]+\.(?:com|net|org|info)", email_input)
empty_list = []
if search_1:
    empty_list.append(search_1)
    print("Email Add")
else:
    print("Invalid Email")
for email in empty_list:
    print(email)
