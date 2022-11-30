# Python Inheritance

class Human:
    leg_count = 4
    def get_gender(self, unknown):
        return unknown

class Man(Human):
    pass

class Woman(Human):
    pass


gender1 = Man()
print(gender1.leg_count, gender1.get_gender("Male"))

gender1 = Man()
print(gender1.get_gender("Male"))

gender2 = Woman()
print(gender2.get_gender("Female"))