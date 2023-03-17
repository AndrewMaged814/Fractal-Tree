from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# global variables
angle_turn = 20
len_multiplier = 0.7



def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def draw_branch(x, y, angle, length, level, color):
    if level == 0:
        return

    x2 = x + math.cos(math.radians(angle)) * length
    y2 = y + math.sin(math.radians(angle)) * length

    # set color for current branch
    glColor3f(*color)

    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x2, y2)
    glEnd()

    # recursively draw sub-branches with slightly shorter length and reduced level
    draw_branch(x2, y2, angle - angle_turn, length * len_multiplier, level - 1, color)
    draw_branch(x2, y2, angle + angle_turn, length * len_multiplier, level - 1, color)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    color = [0.8, 0.6, 0.0]  # yellowish color
    draw_branch(0, -0.8, 90, 0.4, 10, color)
    glFlush()


def keyboard(key, x, y):
    global angle_turn, len_multiplier
    if key == b'q':
        angle_turn += 0.5
    elif key == b'e':
        angle_turn -= 0.5
    
    elif key == b's':
        len_multiplier -= 0.01
    elif key == b'w':
        len_multiplier += 0.01
    glutPostRedisplay()

def main():
    glutInit()
    glutInitWindowSize(700, 700)
    glutCreateWindow("Fractal Tree")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard) 
    glutMainLoop()

if __name__ == '__main__':
    main()
