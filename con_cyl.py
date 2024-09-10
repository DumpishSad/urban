import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_cylinder(radius, height):
    cylinder = gluNewQuadric()
    gluQuadricDrawStyle(cylinder, GLU_LINE)  # Линейный каркас
    gluCylinder(cylinder, radius, radius, height, 30, 30)


def draw_cone(base_radius, height):
    cone = gluNewQuadric()
    gluQuadricDrawStyle(cone, GLU_LINE)  # Линейный каркас
    gluCylinder(cone, base_radius, 0, height, 30, 30)  # Верхний радиус = 0 для конуса


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Устанавливаем перспективу
    gluPerspective(70, (display[0] / display[1]), 0.1, 1000.0)
    glTranslatef(0, 0, -500)
    glRotatef(-90, 1, 0, 0)
    # Основной цикл программы
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Сохраняем текущее состояние
        glPushMatrix()

        # Рисуем цилиндр
        # glScalef(1.7, 1.7, 1.7) scale
        glColor3f(1, 0, 0)  # Устанавливаем цвет цилиндра (красный)
        draw_cylinder(50, 200)  # Цилиндр с радиусом 50 и высотой 200

        # Восстанавливаем состояние
        glPopMatrix()
        glPushMatrix()

        # Перемещаемся так, чтобы вершина конуса была на вершине цилиндра
        glTranslatef(0, 0, -100)  # Сдвигаем по оси Z на высоту цилиндра

        # Рисуем конус
        glColor3f(0, 1, 0)  # Устанавливаем цвет конуса (зелёный)
        draw_cone(50, 100)  # Конус с радиусом основания 50 и высотой 100

        # Восстанавливаем состояние
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
