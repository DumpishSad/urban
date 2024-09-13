import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

light_position = [1.0, 1.0, 1.0, 1.0]
light_ambient = [1.0, 1.0, 1.0, 1.0]
light_diffuse = [0.8, 0.8, 0.8, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]

camera_angle_x = -60
camera_angle_y = 0
camera_distance = 7

texture_id = None


def load_texture(file_name):
    global texture_id
    image = Image.open(file_name)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image_data = image.convert("RGB").tobytes()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)


def draw_cylinder(radius, height):
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glColor4f(0.7, 0.2, 0.0, 0.7)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.2, 0.4, 0.2, 0.4])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.1, 0.1, 0.1, 0.4])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0, 0, 0, 0.4])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, [5])

    glutSolidCylinder(radius, height, 30, 30)


def draw_cone(base_radius, height):
    cone_color = [0.3, 0.3, 0.3, 1]
    cone_specular = [0, 0, 0, 0]
    cone_shininess = [0]

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, cone_color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, cone_specular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, cone_shininess)

    cone = gluNewQuadric()
    gluQuadricDrawStyle(cone, GLU_FILL)
    gluCylinder(cone, base_radius, 0, height, 30, 30)


def draw_cube(size):
    global texture_id

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    vertices = [
        (size / 2, size / 2, -size / 2),
        (-size / 2, size / 2, -size / 2),
        (-size / 2, -size / 2, -size / 2),
        (size / 2, -size / 2, -size / 2),
        (size / 2, size / 2, size / 2),
        (-size / 2, size / 2, size / 2),
        (-size / 2, -size / 2, size / 2),
        (size / 2, -size / 2, size / 2)
    ]

    faces = [
        (vertices[0], vertices[1], vertices[2], vertices[3]),
        (vertices[4], vertices[5], vertices[6], vertices[7]),
        (vertices[0], vertices[3], vertices[7], vertices[4]),
        (vertices[1], vertices[2], vertices[6], vertices[5]),
        (vertices[0], vertices[1], vertices[5], vertices[4]),
        (vertices[3], vertices[2], vertices[6], vertices[7])
    ]

    tex_coords = [
        (1, 1), (0, 1), (0, 0), (1, 0),
    ]

    glBegin(GL_QUADS)
    for face in faces:
        for i, vertex in enumerate(face):
            glTexCoord2fv(tex_coords[i])
            glVertex3fv(vertex)
    glEnd()

    glDisable(GL_TEXTURE_2D)


def draw_sphere(radius):
    mat_ambient = [0.1, 0.1, 0.1, 1.0]
    mat_diffuse = [0.4, 0.4, 0.4, 1.0]
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess = [128.0]

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, mat_shininess)

    glTranslatef(3.0, 0.0, 0.0)

    glutSolidSphere(radius, 100, 100)


def display():
    global light_position, light_diffuse, light_specular

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, 1, 0.1, 1000.0)
    glTranslatef(0, 0, -camera_distance)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    print(light_position)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # СФЕРА
    glPushAttrib(GL_LIGHTING_BIT)
    glPushMatrix()
    draw_sphere(1)
    glPopMatrix()
    glPopAttrib()

    # КОНУС
    glPushAttrib(GL_LIGHTING_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(-1.5, -1, -1)
    glRotatef(-90, 1, 0, 0)
    glRotatef(20, 0, 1, 0)
    draw_cone(1, 2)
    glPopMatrix()
    glPopAttrib()

    # КУБ
    glPushAttrib(GL_LIGHTING_BIT)
    glPushMatrix()
    glTranslatef(0.5, 0, 0)
    glRotatef(-20, 1, 0, 0)
    glRotatef(-5, 0, 1, 0)
    draw_cube(1)
    glPopMatrix()
    glPopAttrib()

    # ЦИЛИНДР
    glPushAttrib(GL_LIGHTING_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPushMatrix()

    glTranslatef(-2, 0, 0)
    glRotatef(100, 1, 0, 0)
    draw_cylinder(0.5, 2)
    glPopMatrix()
    glPopAttrib()

    glFlush()


def keyboard(window, key, scancode, action, mods):
    global light_position, light_diffuse

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    shift = 0.2

    if key == glfw.KEY_UP:
        light_position[1] += shift
    if key == glfw.KEY_DOWN:
        light_position[1] -= shift
    if key == glfw.KEY_LEFT:
        light_position[0] -= shift
    if key == glfw.KEY_RIGHT:
        light_position[0] += shift
    if key == glfw.KEY_PAGE_UP:
        light_position[2] -= shift
    if key == glfw.KEY_PAGE_DOWN:
        light_position[2] += shift


def mouse_motion(w, x, y):
    global light_position
    x *= 2
    x -= 1000
    light_position[0] = (x / 1000 - 1 / 2.0)
    light_position[1] = (0.5 / 2.0 - y / 1000)


def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height)


def keyboard(window, key, scancode, action, mods):
    global light_position, light_diffuse, light_ambient, light_specular

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    shift = 0.2
    color_shift = 0.2  # шаг изменения цвета

    if key == glfw.KEY_UP:
        light_position[1] += shift
    if key == glfw.KEY_DOWN:
        light_position[1] -= shift
    if key == glfw.KEY_LEFT:
        light_position[0] -= shift
    if key == glfw.KEY_RIGHT:
        light_position[0] += shift
    if key == glfw.KEY_PAGE_UP:
        light_position[2] -= shift
    if key == glfw.KEY_PAGE_DOWN:
        light_position[2] += shift

    if key == glfw.KEY_R and action == glfw.PRESS:
        light_diffuse[0] = min(light_diffuse[0] + color_shift, 1.0)
        light_ambient[0] = min(light_ambient[0] + color_shift, 1.0)

    if key == glfw.KEY_R and action == glfw.RELEASE:
        light_diffuse[0] = max(light_diffuse[0] - color_shift, 0.0)
        light_ambient[0] = max(light_ambient[0] - color_shift, 0.0)

    if key == glfw.KEY_G and action == glfw.PRESS:
        light_diffuse[1] = min(light_diffuse[1] + color_shift, 1.0)
        light_ambient[1] = min(light_ambient[1] + color_shift, 1.0)

    if key == glfw.KEY_G and action == glfw.RELEASE:
        light_diffuse[1] = max(light_diffuse[1] - color_shift, 0.0)
        light_ambient[1] = max(light_ambient[1] - color_shift, 0.0)

    if key == glfw.KEY_B and action == glfw.PRESS:
        light_diffuse[2] = min(light_diffuse[2] + color_shift, 1.0)
        light_ambient[2] = min(light_ambient[2] + color_shift, 1.0)

    if key == glfw.KEY_B and action == glfw.RELEASE:
        light_diffuse[2] = max(light_diffuse[2] - color_shift, 0.0)
        light_ambient[2] = max(light_ambient[2] - color_shift, 0.0)

    if key == glfw.KEY_A and action == glfw.PRESS:
        light_ambient = [min(c + color_shift, 1.0) for c in light_ambient]

    if key == glfw.KEY_A and action == glfw.RELEASE:
        light_ambient = [max(c - color_shift, 0.0) for c in light_ambient]


def init():
    glutInit()
    if not glfw.init():
        raise Exception("GLFW can not be initialized!")
    window = glfw.create_window(1000, 1000, "Hello World", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window can not be created!")
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    load_texture("bricks.bmp")

    glfw.set_key_callback(window, keyboard)
    glfw.set_cursor_pos_callback(window, mouse_motion)

    while not glfw.window_should_close(window):
        display()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    init()