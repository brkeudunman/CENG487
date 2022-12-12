# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2

# References:
# https://stackoverflow.com/questions/72539296/pyopengl-how-to-render-text
# https://www.opengl.org/resources/libraries/glut/spec3/node70.html
# https://www.ascii-code.com/


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from shapes.pyFiles.cube import Cube
from shapes.pyFiles.pyramid import Pyramid
from shapes.pyFiles.simsObj import SimsPyramid

import time

from shapes.pyFiles.sphere import Sphere
from shapes.pyFiles.tori import Tori
from tools.camera import Camera
from tools.keyboardControl import KeyboardControl
from scene import Scene

# Number of the glut window.
window = 0

# Initializing the scene with empty object array
scene = Scene([])

# Initializing cube
cube_one = Cube()
# Initializing pyramid
pyramid_one = Pyramid()
# Initializing simsObj
sims = SimsPyramid()
# Initializing Sphere
sphere = Sphere()

tori = Tori()

# Pick one to draw
arr = [cube_one, pyramid_one, sims, sphere, tori]

for model in arr:
    scene.appendModelToScene(model)

# Camera
camera = Camera([3, 3, 3])


# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):  # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
    glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
    glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    # The main drawing function.


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear The Screen And The Depth Buffer
    glLoadIdentity()  # Reset The View
    
    # Displaying Text
    display()
    # Update Camera
    camera.cameraUpdate()
    # Draw Scene
    scene.drawScene()
    
    time.sleep(0.05)  # To give smoothness of movement
    glutSwapBuffers()


i = 0
scene.drawModelByIndex(i)

def display():
    Scene.text(0, 180, (1, 1, 1),
            "Press + to go for next object\n"
            "Press - to go for previous object\n"
            "Press 1 for cube \n"
            "Press 2 for pyramid\n"
            "Press 3 for diamond\n"
            "Press 4 for sphere\n"
            "Press 5 for tori\n"
            "Press ESC for Exit")

    Scene.text(0, 450, (1, 1, 1),
            "Camera Position: "
            "X: "
            f"{str(camera.x_cam)[0:3]}\t"
            "Y: "
            f"{str(camera.y_cam)[0:3]}\t"
            "Z: """
            f"{str(camera.z_cam)[0:3]}\t"
            )
    Scene.text(360, 100, (1, 1, 1),
            "Camera Control: \n"
            'W,A,S,D\n'
            'Space and Quotation button\n'
            'Press F to reset the camera'
            )
    

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(key, x, y):
    global x_cam, z_cam, y_cam
    global i
    # If escape is pressed, kill everything.
    # ord() is needed to get the keycode
    KeyboardControl.controlMainScene(key,arr,camera,scene,i)

def main():
    global window
    glutInit(sys.argv)

    # Select type of Display mode:
    #  Double buffer
    #  RGBA color
    #  Alpha components supported
    #  Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # get a 640 x 480 window
    glutInitWindowSize(640, 480)

    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

    # Okay, like the C version we retain the window id to use when closing, but for those of you new
    # to Python (like myself), remember this assignment would make the variable local and not global
    # if it weren't for the global declaration at the start of main.
    window = glutCreateWindow("CENG487 Development Env Test")

    # Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
    # set the function pointer and invoke a function to actually register the callback, otherwise it
    # would be very much like the C version of the code.
    glutDisplayFunc(DrawGLScene)

    # Uncomment this line to get full screen.
    # glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    # Initialize our window.
    InitGL(640, 480)

    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.

print("Hit ESC key to quit.")

main()
