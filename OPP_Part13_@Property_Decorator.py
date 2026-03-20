# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------
class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return f"Hi:{self.name}"

    @property
    def age_in_day(self):
        return f"Age:{self.age * 365}"


one = Member("Ahmad", 25)
print(one.name)
print(one.age)
print(one.say_hi())
print(one.age_in_day)  # ()
