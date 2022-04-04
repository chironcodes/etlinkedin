# _author_ = ["Diego Alves", "Adilton Costa Anna"]
# _license_ = "Beerware"
# _version_ = "0.0.1"
class User():

    def __init__(self, email, password):
        try:
            self._email = email
            self._password = password
        except Exception as e:
            print(str(e))

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if new_email != '' and isinstance(new_email, str):
            self._email = new_email
        else:
            print("Please enter a valid email")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if new_password != '' and isinstance(new_password, str):
            self._password = new_password
        else:
            print("Please enter a valid password")
