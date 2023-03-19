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

    # enable anti-aliasing
    glEnable(GL_BLEND)
    glEnable(GL_LINE_SMOOTH)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glLineWidth(1.0)



def draw_branch(x, y, angle, length, level, color1, color2):
    if level == 0:
        return

    x2 = x + math.cos(math.radians(angle)) * length
    y2 = y + math.sin(math.radians(angle)) * length

    # calculate color gradient for current branch
    color = [(color2[i] - color1[i]) / level + color1[i] for i in range(3)]

    # set color for current branch
    glColor3f(*color)

    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x2, y2)
    glEnd()

    # recursively draw sub-branches with slightly shorter length and reduced level
    draw_branch(x2, y2, angle - angle_turn, length * len_multiplier, level - 1, color1, color2)
    draw_branch(x2, y2, angle + angle_turn, length * len_multiplier, level - 1, color1, color2)



def display():
    glClear(GL_COLOR_BUFFER_BIT)
    tree_color1 = [0.8, 0.4, 0.0]
    tree_color2 = [0.0, 0.4, 0.0]     
    draw_branch(0, -0.8, 90, 0.4, 10, tree_color1, tree_color2)
    glFlush()


def keyboard(key, x, y):
    global angle_turn, len_multiplier, depth_mul
    if key == b'q':
        angle_turn += 0.5
    elif key == b'e':
        angle_turn -= 0.5
    
    elif key == b's':
        len_multiplier -= 0.001
    elif key == b'w':
        len_multiplier += 0.001
        
        
    glutPostRedisplay()

def main():
    glutInit()
    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)
    window_width = int(screen_width * 0.5)
    window_height = int(screen_height) 
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("Fractal Tree")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard) 
    glutMainLoop()


if __name__ == '__main__':
    main()
