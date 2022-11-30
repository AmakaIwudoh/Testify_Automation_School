# Python Polymorphism

class Human:
    leg_count = 4
    def get_gender(self, unknown):
        return unknown

class Man(Human):
    def get_gender(self, man):
        return man

class Woman(Human):
    def get_gender(self, woman):
        return woman


gender1 = Man()
print(gender1.get_gender("man"))

gender2 = Woman()
print(gender2.get_gender("woman"))