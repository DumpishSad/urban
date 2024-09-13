# 1. Изобразить каркасный куб со стороной 250 и с центром в точке O (40,30), и описать
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

vertices = [
    (125, 125, -125),
    (-125, 125, -125),
    (-125, -125, -125),
    (125, -125, -125),
    (125, 125, 125),
    (-125, 125, 125),
    (-125, -125, 125),
    (125, -125, 125)
]

edges = (
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
)

cube_x = 0
sphere_z = 0

target_cube_x = 250
target_sphere_z = -150

start_cube_x = 0
start_sphere_z = 0

move_speed = 2
moving = False

move_forward = True


def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_sphere(radius):
    sphere = gluNewQuadric()
    gluQuadricDrawStyle(sphere, GLU_LINE)
    gluSphere(sphere, radius, 30, 30)


def main():
    global cube_x, sphere_z, moving, move_forward

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(90, (display[0] / display[1]), 0.1, 1000.0)
    glTranslatef(40, 30, -500)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    moving = True
                    move_forward = not move_forward

        if moving:
            if move_forward:
                if cube_x < target_cube_x:
                    cube_x += move_speed
                    if cube_x > target_cube_x:
                        cube_x = target_cube_x

                if sphere_z > target_sphere_z:
                    sphere_z -= move_speed
                    if sphere_z < target_sphere_z:
                        sphere_z = target_sphere_z
            else:
                if cube_x > start_cube_x:
                    cube_x -= move_speed
                    if cube_x < start_cube_x:
                        cube_x = start_cube_x

                if sphere_z < start_sphere_z:
                    sphere_z += move_speed
                    if sphere_z > start_sphere_z:
                        sphere_z = start_sphere_z

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(cube_x, 0, 0)
        glColor3f(1, 1, 1)
        draw_cube()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0, sphere_z)
        glColor3f(0, 0, 1)
        draw_sphere(math.sqrt(3) * 250 / 2)
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
