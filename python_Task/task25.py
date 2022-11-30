# Python Static Method

class Utilities:

    def print_name(name):
        return name

    @staticmethod
    def print_age(age):
        return age

Utilities.print_name = staticmethod(Utilities.print_name)

print(Utilities.print_name("Name: " + "Amaka"))
print(Utilities.print_age(6))