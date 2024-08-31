class User:
    """
    Класс пользователь, содержащий атрибуты: nickname, password, age
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        print(hash(self.password))
        return hash(self.password)
