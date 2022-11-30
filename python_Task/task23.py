# Python Data Abstraction

class User:
    _password = "password"

    def get_password(self):
        return self._password

class ActiveUser(User):
        pass

        def get_password(self):
            return "Password: " + "********"

Amaka = ActiveUser()
print(Amaka.get_password())


