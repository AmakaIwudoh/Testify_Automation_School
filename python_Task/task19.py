# Python OOP Methods

class Human:
    leg_count = 4
    can_walk = True

    def get_description(self, str):
        return str

    def get_leg_count(self, leg_count):
        return leg_count

amaka = Human()
print(amaka.leg_count)
print(amaka.get_description("This is human"))
print(amaka.get_leg_count(2), amaka.can_walk)
