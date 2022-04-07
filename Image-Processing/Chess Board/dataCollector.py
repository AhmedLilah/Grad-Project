from ImageHelpers import *
# from gpiozero import Button 
# captureSwitch = Button(2)

if __name__ == '__main__':
    i = 0
    while (True):
        # if capturSwitch.is_pressed:
        # key = cv2.waitKey(0) # waits for a key to be pressed
        key = input('do you wnat to catpure (y or n): ')
        if key == 'y':
            img = captureImage(showImage= False)
            cv2.imwrite('000000',img)
            ret , pts = findPoints(img, inputMode= 'image', showPoints= False)
            if ret:
                img = fourPointsTransform(img, pts, returnMode = 'image', showWarpedImage= False)
                splitBoard(img, 'image', 'store', True, name='Board' + str(i) + 'Square')
                i += 1
        elif key == 'n':
            print('Data Collector Is Out...')
            break