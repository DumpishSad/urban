class User:
    """
    Класс пользователь, содержащий атрибуты: nickname, password, age
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        print(self.password)

    def __str__(self):
        return f'{self.nickname}'
