# Python Encapsulation

class Hunt:
    _weapon = "Assault Rifle"

    def get_weapon(self, Not_Available):
        return Not_Available

    def get_name(self):
        return "Weapon: " + self._weapon

hunt = Hunt()
print(hunt.get_weapon("Not_Available"))
print(hunt.get_name())

