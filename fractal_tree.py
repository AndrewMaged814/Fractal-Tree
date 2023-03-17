from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def draw_branch(x, y, angle, length, level):
    if level == 0:
        return

    x2 = x + math.cos(math.radians(angle)) * length
    y2 = y + math.sin(math.radians(angle)) * length

    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x2, y2)
    glEnd()

    draw_branch(x2, y2, angle - 20, length * 0.7, level - 1)
    draw_branch(x2, y2, angle + 20, length * 0.7, level - 1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    draw_branch(0, -0.8, 90, 0.4, 10)
    glFlush()

def main():
    glutInit()
    glutInitWindowSize(700, 700)
    glutCreateWindow("Fractal Tree")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()
