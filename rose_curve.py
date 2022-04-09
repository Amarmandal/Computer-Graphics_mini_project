from cmath import sin
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math 

w, h = 800, 600
window_position_x = 100
window_position_y = 0


class RoseFamily:
    def setWindow(self, left, right, bottom, top):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(left, right, bottom, top)

    
    def setViewport(self, left, bottom, width, height):
        glViewport(left, bottom, width, height)

    def draw_rose_sm_h_axis(self, xc, yc, a, n):
        glPointSize(2.0)
        glBegin(GL_POINTS)

        for degree in range(0, 180):
            radian = degree * math.pi / 180
            r = a * math.cos(n * radian)
            x = xc + r * math.cos(radian)
            y = yc + r * math.sin(radian)
            xs = xc + r * math.cos(-radian)
            ys = yc + r * math.sin(-radian)

            glVertex2f(x, y)
            glVertex2f(xs, ys)
           
        glEnd()
        glFlush()

    def draw_rose_sm_v_axis(self, xc, yc, a, n):
        glPointSize(2.0)
        glBegin(GL_POINTS)

        for degree in range(90, 270):
            radian = degree * math.pi / 180
            r = a * math.sin(n * radian)
            x = xc + r * math.cos(radian)
            y = yc + r * math.sin(radian)
            xs = xc - r * math.cos(-radian)
            ys = yc - r * math.sin(-radian)

            glVertex2f(x, y)
            glVertex2f(xs, ys)
           
        glEnd()
        glFlush()

   

    def showScreen(self):
        glClear(GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT)
        glColor3f(0.0, 1.0, 0.0)
        self.setWindow(0, 800, 0, 600)
        self.setViewport(0, 0, 800, 600)
        self.draw_rose_sm_h_axis(100, 100, 50, 3)
        glColor3f(1.0, 1.0, 0.0)
        self.draw_rose_sm_h_axis(200, 200, 60, 4)
        glColor3f(1.0, 0.0, 1.0)
        self.draw_rose_sm_h_axis(300, 300, 65, 5)
        glColor3f(1.0, 1.0, 0.4)
        self.draw_rose_sm_h_axis(400, 400, 70, 6)
        glutSwapBuffers()


def main():
    obj_1 = RoseFamily()
   
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(window_position_x, window_position_y)
    glutCreateWindow("Rose Family")
    glutDisplayFunc(obj_1.showScreen)
    glutIdleFunc(obj_1.showScreen)
    glutMainLoop()


if __name__ == "__main__":
    main()