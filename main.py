import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


def requests_():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Полученные данные:", data)
    else:
        print(f"Ошибка при запросе данных. Статус: {response.status_code}")


def pandas_():
    df = pd.read_csv('matrix0.csv')

    print("Первые 5 строк данных:")
    print(df.head())

    print("\nСтатистика по числовым данным:")
    print(df.describe())


def numpy_():
    arr = np.array([1, 2, 3, 4, 5])

    squared = np.square(arr)
    sum_arr = np.sum(arr)
    mean_arr = np.mean(arr)

    print(f"Исходный массив: {arr}")
    print(f"Массив возведённый в квадрат: {squared}")
    print(f"Сумма элементов массива: {sum_arr}")
    print(f"Среднее значение массива: {mean_arr}")


def matplotlib_():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(figsize=(10, 5))

    # синус
    plt.subplot(1, 2, 1)
    plt.plot(x, y1, label='sin(x)', color='blue')
    plt.title('График синуса')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.legend()

    # косинус
    plt.subplot(1, 2, 2)
    plt.plot(x, y2, label='cos(x)', color='red')
    plt.title('График косинуса')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


def pillow_():
    image = Image.open('dysya.jpg')
    resized_image = image.resize((800, 600))
    blurred_image = resized_image.filter(ImageFilter.BLUR)
    blurred_image.save('dysya.png')


requests_()
print('-' * 100)
pandas_()
print('-' * 100)
numpy_()
print('-' * 100)
matplotlib_()
print('-' * 100)
pillow_()
