import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time


def draw_cylinder(radius, height):
    cylinder = gluNewQuadric()
    gluQuadricDrawStyle(cylinder, GLU_LINE)
    gluCylinder(cylinder, radius, radius, height, 30, 30)


def draw_cone(base_radius, height):
    cone = gluNewQuadric()
    gluQuadricDrawStyle(cone, GLU_LINE)
    gluCylinder(cone, base_radius, 0, height, 30, 30)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(70, (display[0] / display[1]), 0.1, 1000.0)
    glTranslatef(0, 0, -700)
    glRotatef(-70, 1, 0, 0)

    scale_factor = 1.0
    target_scale = 1.0
    scaling_speed = 0.02

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if target_scale == 1.0:
                        target_scale = 1.7
                    else:
                        target_scale = 1.0

        if scale_factor < target_scale:
            scale_factor += scaling_speed
            if scale_factor > target_scale:
                scale_factor = target_scale
        elif scale_factor > target_scale:
            scale_factor -= scaling_speed
            if scale_factor < target_scale:
                scale_factor = target_scale

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glScalef(scale_factor, scale_factor, scale_factor)
        glColor3f(1, 0, 0)
        draw_cylinder(50, 200)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0, -100)
        glColor3f(0, 1, 0)
        draw_cone(50, 100)
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
