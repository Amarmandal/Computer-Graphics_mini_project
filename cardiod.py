from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math 

w, h = 800, 600
window_position_x = 100
window_position_y = 0


class CardiodFamily:
    def __init__(self, a):
        self.a = a
        

    def setWindow(self, left, right, bottom, top):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(left, right, bottom, top)

    
    def setViewport(self, left, bottom, width, height):
        glViewport(left, bottom, width, height)

    def draw_horizontal_cardiod(self, cardiod_direction, xc, yc):
        glPointSize(2.0)
        glBegin(GL_POINTS)

        for degree in range(0, 180):
            radian = degree * math.pi / 180
            if cardiod_direction == "left": 
                r = self.a - self.a * math.cos(radian)
            else: 
                r = self.a + self.a * math.cos(radian)

            x = xc + r * math.cos(radian)
            y = yc + r * math.sin(radian)
            xs = xc + r * math.cos(-radian)
            ys = yc + r * math.sin(-radian)

            glVertex2f(x, y)
            glVertex2f(xs, ys)
           
        glEnd()
        glFlush()

    def draw_vertical_cardiod(self, cardiod_direction, xc, yc):
        glPointSize(2.0)
        glBegin(GL_POINTS)

        for degree in range(90, 270):
            radian = degree * math.pi / 180
            if cardiod_direction == "up": 
                r = self.a + self.a * math.sin(radian)
            else: 
                r = self.a - self.a * math.sin(radian)

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
        self.draw_horizontal_cardiod("left", 200, 250)
        glColor3f(1.0, 0.0, 0.0)
        self.draw_horizontal_cardiod("right", 300, 250)
        glColor3f(0.0, 0.0, 1.0)
        self.draw_vertical_cardiod("up", 500, 225)
        glColor3f(0.0, 1.0, 1.0)
        self.draw_vertical_cardiod("down", 650, 275)
        glutSwapBuffers()


def main():
    a = int(input("Enter the value of a: "))

    if(a < 0):
        return print("a and b > 0")

    obj_1 = CardiodFamily(a)
   
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(window_position_x, window_position_y)
    glutCreateWindow("Cardiod Family")
    glutDisplayFunc(obj_1.showScreen)
    glutIdleFunc(obj_1.showScreen)
    glutMainLoop()


if __name__ == "__main__":
    main()