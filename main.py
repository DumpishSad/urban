import datetime
import multiprocessing


def read_info(name):
    with open(name, 'r') as f:
        all_data = [line for line in iter(f.readline, '')]


filenames = [f'file_{number}.txt' for number in range(1, 5)]


# Линейный вызов
def lin_main():
    start = datetime.datetime.now()
    list(map(read_info, filenames))
    end = datetime.datetime.now()
    print(f'Линейный вызов: {end - start}')


# Многопроцессный
def mul_main():
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'Многопроцессный вызов: {end - start}')


if __name__ == '__main__':
    lin_main()
    mul_main()
