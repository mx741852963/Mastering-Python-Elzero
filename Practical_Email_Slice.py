# ---------------
# -- Practical Email Slice --
# ---------------

theName = input("What\'s your name?").strip().capitalize()
theEmail = input("What\'s your Email?").strip()
theUserName = theEmail[0:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]
print(f"Hello {theName} Your Email is: {theEmail}")
print(f"Your Username is {theUserName} \n Your Website is {theWebsite} ")
# email = "ahmad@aljmal.org"
# print(email[0:email.index("@")])
