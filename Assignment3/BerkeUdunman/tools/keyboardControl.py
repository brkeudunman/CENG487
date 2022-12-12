# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2

from OpenGL.GLUT import glutLeaveMainLoop

from scene import Scene


class KeyboardControl:
    
    @staticmethod
    def controlMainScene(key,arr,camera,scene,i):
        if ord(key) == 27:
            KeyboardControl.escape()
        elif ord(key) == 43:
            # + key,
            if i == len(arr) - 1:
                i = 0
            else:
                i += 1
            KeyboardControl.draw(scene,i)
            return
        elif ord(key) == 45:
            # - key,
            if abs(i) == len(arr) - 1:
                i = 0
            else:
                i -= 1
            KeyboardControl.draw(scene,i)
            return
        elif ord(key) == 49:
            # 1 key,
            i = 0
            KeyboardControl.draw(scene,i)
            return
        elif ord(key) == 50:
            # 2 key,
            i = 1
            KeyboardControl.draw(scene,i)
            return
        elif ord(key) == 51:
            # 3 key,
            i = 2
            KeyboardControl.draw(scene,i)
            return
        elif ord(key) == 52:
            # 4 key,
            i = 3
            KeyboardControl.draw(scene,i)
            return
        elif ord(key) == 53:
            # 5 key,tori
            i = 4
            KeyboardControl.draw(scene,i)
            return
        elif ord(key) == 97:
            # 'a' key
            KeyboardControl.cameraMovement(camera,"x",1)
        elif ord(key) == 100:
            # 'd' key
            KeyboardControl.cameraMovement(camera,"x",-1)
        elif ord(key) == 119:
            # 'w' key
            KeyboardControl.cameraMovement(camera,"z",1)
        elif ord(key) == 115:
            # 's' key
            KeyboardControl.cameraMovement(camera,"z",-1)
        elif ord(key) == 32:
            # 'space' key
            KeyboardControl.cameraMovement(camera,"y",1)
        elif ord(key) == 34:
            # 'shift' key
            KeyboardControl.cameraMovement(camera,"y",-1)
        elif ord(key) == 102:
            # 'f' key
            KeyboardControl.cameraMovement(camera,"reset",0)

        
    
    @staticmethod
    def escape():
        glutLeaveMainLoop()
        return

    @staticmethod
    def draw(scene,i):
        scene.clearScene()
        scene.drawModelByIndex(i)
        return
    
    @staticmethod
    def cameraMovement(camera,axis,sign):
        if(axis=="x"):
            camera.x_cam=camera.x_cam + sign*0.1
        elif axis=="y":
            camera.y_cam=camera.y_cam + sign*0.1
        elif axis=="z":
            camera.z_cam=camera.z_cam + sign*0.1
        else:
            camera.x_cam = 3  # reset the camera
            camera.y_cam = 3
            camera.z_cam = 3
        
        