# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attributes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------
# class Member:
#     def __init__(self, name):
#         self.name = name  # Public
#
#
# one = Member("One")
# print(one.name)
# one.name = "Ahmad"
# print(one.name)


# class Member:
#     def __init__(self, name):
#         self._name = name  # Protected
#
# one = Member("One")
# print(one._name)
# one._name = "Ahmad"
# print(one._name)

class Member:
    def __init__(self, name):
        self.__name = name  # Privet

    def say_hi(self):
        return f"Hi:{self.__name}"


one = Member("Ahmad")
# print(one.__name)
# one._name = "Ahmad"
# print(one._name)
print(one.say_hi())
print(one._Member__name)
