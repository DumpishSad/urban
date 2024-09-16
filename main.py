from datetime import datetime
from threading import Thread
from time import sleep


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_stop = datetime.now()
time_res = time_stop - time_start
print(f'Время работы функций {time_res}')

time2_start = datetime.now()
thr_first = Thread(target=wite_words, args=(10, 'example1.txt'))
thr_sec = Thread(target=wite_words, args=(30, 'example2.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example3.txt'))
the_fourth = Thread(target=wite_words, args=(100, 'example4.txt'))

thr_first.start()
thr_sec.start()
thr_third.start()
the_fourth.start()

thr_first.join()
thr_sec.join()
thr_third.join()
the_fourth.join()
time_stop = datetime.now()
time_res = time_stop - time2_start
print(f'Работа потоков {time_res}')

# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Время работы функций 0:00:37.179174
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example4.txt
# Завершилась запись в файл example3.txt
# Работа потоков 0:00:21.821973