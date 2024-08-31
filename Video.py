class Video:
    """
    Класс видео, содержащий атрибуты: title, duration, time_now, adult_mode
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"{self.title}"