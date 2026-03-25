# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------
class Member:
    def __init__(self, name):
        self.__name = name  # Privet

    def say_hi(self):
        return f"Hi:{self.__name}"

    def get_name(self):  # Getter
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


one = Member("Ahmad")
# one._Member__name = "ali"
# print(one._Member__name)
# print(one.get_name())
one.set_name("ali")
print(one.get_name())
