from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math 

w, h = 800, 600
window_position_x = 100
window_position_y = 0


class LimaconFamily:
    def setWindow(self, left, right, bottom, top):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(left, right, bottom, top)

    
    def setViewport(self, left, bottom, width, height):
        glViewport(left, bottom, width, height)

    def draw_horizontal_limacon(self, xc, yc, a, b, limacon_dir = "right"):
        glPointSize(2.0)
        glBegin(GL_POINTS)

        for degree in range(0, 180):
            radian = degree * math.pi / 180
            if limacon_dir == "left": 
                r = a - b * math.cos(radian)
            else: 
                r = a + b * math.cos(radian)

            x = xc + r * math.cos(radian)
            y = yc + r * math.sin(radian)
            xs = xc + r * math.cos(-radian)
            ys = yc + r * math.sin(-radian)

            glVertex2f(x, y)
            glVertex2f(xs, ys)
           
        glEnd()
        glFlush()

    def draw_vertical_limacon(self, xc, yc, a, b, limacon_dir = "up"):
        glPointSize(2.0)
        glBegin(GL_POINTS)

        for degree in range(90, 270):
            radian = degree * math.pi / 180
            if limacon_dir == "up": 
                r = a + b * math.sin(radian)
            else: 
                r = a - b * math.sin(radian)

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
        self.draw_horizontal_limacon(100, 200, 30, 60)
        glColor3f(1.0, 0.0, 0.0)
        self.draw_horizontal_limacon(250, 200, 40, 40)
        glColor3f(0.0, 0.0, 1.0)
        self.draw_horizontal_limacon(400, 200, 40, 30)
        glColor3f(0.0, 1.0, 1.0)
        self.draw_horizontal_limacon(550, 200, 90, 45)

        #vertical Limacon
        self.draw_vertical_limacon(100, 400, 30, 60)
        glColor3f(1.0, 0.0, 0.0)
        self.draw_vertical_limacon(250, 400, 40, 40)
        glColor3f(0.0, 0.0, 1.0)
        self.draw_vertical_limacon(400, 400, 40, 30)
        glColor3f(0.0, 1.0, 1.0)
        self.draw_vertical_limacon(600, 400, 90, 45)
        glutSwapBuffers()


def main():
    obj_1 = LimaconFamily()
   
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(window_position_x, window_position_y)
    glutCreateWindow("Limacon Family")
    glutDisplayFunc(obj_1.showScreen)
    glutIdleFunc(obj_1.showScreen)
    glutMainLoop()


if __name__ == "__main__":
    main()