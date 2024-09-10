# Вариант 49
# Изобразить каркасный куб со стороной 250 и с центром в точке O (40,30), и описать
# вокруг него каркасную сферу.
# 2. Выполнить сдвиг куба на dх=250, сферы на dz=-150.
# 3. Изобразить конус и цилиндр, где вершина конуса является центром основания
# цилиндра.
# 4. Промасштабировать цилиндр с коэффициентом 1,7

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Координаты вершин куба относительно центра (0, 0)
vertices = [
    (125, 125, -125),  # Верхняя передняя правая
    (-125, 125, -125),  # Верхняя передняя левая
    (-125, -125, -125),  # Нижняя передняя левая
    (125, -125, -125),  # Нижняя передняя правая
    (125, 125, 125),  # Верхняя задняя правая
    (-125, 125, 125),  # Верхняя задняя левая
    (-125, -125, 125),  # Нижняя задняя левая
    (125, -125, 125)  # Нижняя задняя правая
]

# Пары вершин, образующих рёбра куба
edges = (
    (0, 1), (1, 2), (2, 3), (3, 0),  # Передняя грань
    (4, 5), (5, 6), (6, 7), (7, 4),  # Задняя грань
    (0, 4), (1, 5), (2, 6), (3, 7)  # Соединяющие рёбра
)


# Функция рисования каркасного куба
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


# Функция рисования каркасной сферы
def draw_sphere(radius):
    sphere = gluNewQuadric()  # Создаем сферу
    gluQuadricDrawStyle(sphere, GLU_LINE)  # Линейный каркас
    gluSphere(sphere, radius, 30, 30)  # Рисуем сферу с заданным радиусом


# Функция для сдвига куба по оси X на dx = 250
def move_cube():
    glTranslatef(250, 0, 0)  # Сдвигаем куб по оси X на 250


# Функция для сдвига сферы по оси Z на dz = -150
def move_sphere():
    glTranslatef(0, 0, -150)  # Сдвигаем сферу по оси Z на -150


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Устанавливаем перспективу
    gluPerspective(90, (display[0] / display[1]), 0.1, 1000.0)

    # Изначальная позиция куба (центр в O(40, 30))
    # Выполняем изначальное смещение куба в точку O(40, 30)
    glTranslatef(40, 30, -500) # x, y, z


    # Основной цикл программы
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        # Рисуем куб в текущем положении (центр в O(40, 30))
        # move_cube()
        glColor3f(1, 1, 1)
        draw_cube()

        # Описываем вокруг куба каркасную сферу с радиусом 216.5
        # move_sphere()
        glColor3f(0, 0, 1)
        draw_sphere((math.sqrt(3) * 250 / 2))
        glPopMatrix()


        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
