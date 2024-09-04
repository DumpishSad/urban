import os
import time
import itertools
directory = os.getcwd()

for dirpath, dirnames, filenames in itertools.islice(os.walk(directory), 2):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))


path = r'C:\Users\alex3\PycharmProjects\urban\venv\Lib\site-packages\wheel-0.38.4.dist-info\entry_points.txt'

mtime = os.path.getmtime(path)
print('Дата последнего изменения: ',time.ctime(mtime))
print('Размер в байтах:', os.path.getsize(path))
print('Имя каталога:', os.path.dirname(path))
