from tkinter import Y
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
            playVideo()
            img = captureImage(showImage= False)
            # img = cv2.imread("BoardTest2.png")
            procBoard,invProcBoard = boardPreProcessor(img, True)
            # cv2.imwrite('000000.png',img)
            # cv2.imwrite('000000pro.png',procBoard)
            # cv2.imwrite('000000proInv.png',invProcBoard)
            ret1 , pts1 = findPoints(img, inputMode= 'image', showPoints= False)
            ret2 , pts2 = findPoints(procBoard, inputMode= 'image', showPoints= False)
            ret3 , pts3 = findPoints(invProcBoard, inputMode= 'image', showPoints= False)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            if ret1:
                print("ret1 successful")
                img = fourPointsTransform(img, pts1, returnMode = 'image', showWarpedImage= True)
                splitBoard(img, 'image', 'return', True, name='Board' + str(i) + 'Square')
                i += 1
            elif ret2 :
                print("ret2 successful")
                img = fourPointsTransform(img, pts2, returnMode = 'image', showWarpedImage= True)
                splitBoard(img, 'image', 'return', True, name='Board' + str(i) + 'Square')
                i += 1
            elif ret3 :
                print("ret3 successful")
                img = fourPointsTransform(img, pts3, returnMode = 'image', showWarpedImage= True)
                splitBoard(img, 'image', 'return', True, name='Board' + str(i) + 'Square')
                i += 1
            else:
                print("board identification Failed")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        elif key == 'n':
            print('Data Collector Is Out...')
            break