from ImageHelpers import *
from gpiozero import Button 
from os import sleep

captureSwitch = Button(2)

if __name__ == '__main__':
    i = 0 
    while (True):
        if capturSwitch.is_pressed:
            img = captureImage(showImage= True)
            ret , pts = findPoints(image= img, inputMode= 'image', showPoints= False)
            if ret:
                img = fourPointsTransform(image= img, pts= pts, returnMode = 'image', showWarpedImage= False)
                splitBoard(img, 'image', 'store', True, name='Board' + str(i) + 'Square')
                i += 1