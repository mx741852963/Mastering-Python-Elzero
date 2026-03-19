# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------

class Member:
    not_allowed_names = ["Hell", "Shit", "Baloot"]
    users_num = 0

    @classmethod
    def show_user_count(cls):

        print(f"We Have {cls.users_num} Users in Our System")

    @staticmethod
    def say_hello():
        print("Hello Our System")

    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.users_num += 1

    def fullname(self):
        if self.fname in Member.not_allowed_names:
            raise ValueError("Name not allowed")
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

    def delete_user(self):
        Member.users_num -= 1
        return f"User {self.fname} Deleted"


print(Member.users_num)
member_one = Member("ahmad", "ali", "karem", "male")
member_two = Member("ali", "karem", "ahmad", "male")
member_three = Member("mona", "ahmad", "ali", "female")
member_four = Member("Hell", "dd", "ad", "female")

# print(dir(member_one))
# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.lname)
# print(member_three.mname)
# print(member_one.fullname())
# print(member_two.say_hi())
# print(member_three.say_hi())
print(member_one.get_all())
# print(member_four.get_all())
# print(dir(Member))
print(Member.users_num)
print(member_four.delete_user())
print(Member.users_num)
print("=" * 50)
Member.show_user_count()
print("=" * 50)
# Note 99999
# print(member_one.fullname())
# print(Member.fullname(member_one))
Member.say_hello()
