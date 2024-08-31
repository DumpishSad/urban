import time

from User import User


class UrTube:
    """
    Класс UrTube -  видеохостинг. Содержит атрибуты users, videos, current_user.
    """
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for movie_cur in video:
            flag = True
            for movie in self.videos:
                if movie.title.lower() == movie_cur.title.lower():
                    flag = False
                    break
            if flag:
                self.videos.append(movie_cur)

    def get_videos(self, name_video):
        result = []
        for movie_name in self.videos:
            if name_video.lower() in movie_name.title.lower():
                result.append(movie_name)
            else:
                continue
        return result

    def watch_video(self, movie_name):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie_name in video.title:
                    for i in range(1, video.duration + 1):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __repr__(self):
        return f"{self.users}"
