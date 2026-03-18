# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------


class Member:
    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

    def fullname(self):
        return f'{self.fname} {self.mname} {self.lname}'

    def say_hi(self):
        if self.gender == "male":
            return f'Hello Mr {self.fname}_{self.lname}'.title()
        elif self.gender == "female":
            return f'Hello Ms {self.fname}_{self.mname}'.title()
        else:
            return None

    def get_all(self):
        return f"{self.say_hi()} , Your Full Name Is : {self.fullname()} "


member_one = Member("ahmad", "ali", "karem", "male")
member_two = Member("ali", "karem", "ahmad", "male")
member_three = Member("mona", "ahmad", "ali", "female")
# print(dir(member_one))
# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.lname)
# print(member_three.mname)
# print(member_one.fullname())
# print(member_two.say_hi())
# print(member_three.say_hi())
print(member_one.get_all())
