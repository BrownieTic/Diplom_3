import random as r

class UserDataRandom:
    def data_random():
        name = "Ваня" + str(r.randint(100, 9999))
        login = str(r.randint(100, 9999)) + "@ya.ru"
        password = "123asd"
        data_random = {
            "name": name,
            "login": login,
            "password": password
        }
        return data_random

class UserData:
    def login_password():
        login_password = {
            "login": "124567@ya.ru",
            "password": "123asd"
        }
        return login_password
    