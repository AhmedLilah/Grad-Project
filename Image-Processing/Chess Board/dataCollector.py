from ImageHelpers import *
# from gpiozero import Button 
# captureSwitch = Button(2)

if __name__ == '__main__':
    i = 0 
    while (True):
        # if capturSwitch.is_pressed:
        k = cv2.waitKey(0) # waits for a key to be pressed
        if k == 10:
            img = captureImage(showImage= True)
            cv2.imshow("captured image", img)
            ret , pts = findPoints(image= img, inputMode= 'image', showPoints= False)
            if ret:
                img = fourPointsTransform(image= img, pts= pts, returnMode = 'image', showWarpedImage= False)
                splitBoard(img, 'image', 'store', True, name='Board' + str(i) + 'Square')
                i += 1
        elif k == 27:
            break
        else:
            continue
        