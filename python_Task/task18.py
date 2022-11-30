# Python OOP Attributes

class Human:

    leg_count = 4
    can_walk = True

    def __init__(self, leg_count,can_walk):
        self.leg_count = leg_count
        self.can_walk = can_walk


amaka = Human(4,True)
print(amaka.leg_count)
print(amaka.can_walk)

