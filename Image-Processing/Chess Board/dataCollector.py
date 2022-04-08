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
            # img = captureImage(showImage= False)
            img = cv2.imread("BoardTest2.png")
            cv2.imwrite('000000.png',img)
            procBoard,invProcBoard = boardPreProcessor(img, True)
            cv2.imwrite('000000pro.png',procBoard)
            cv2.imwrite('000000proInv.png',invProcBoard)
            ret1 , pts1 = findPoints(procBoard, inputMode= 'image', showPoints= False)
            ret2 , pts2 = findPoints(invProcBoard, inputMode= 'image', showPoints= False)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            if ret1:
                print("ret1 successful")
                img = fourPointsTransform(img, pts1, returnMode = 'image', showWarpedImage= True)
                splitBoard(img, 'image', 'store', True, name='Board' + str(i) + 'Square')
                i += 1
            elif ret2 :
                print("ret2 successful")
                img = fourPointsTransform(img, pts2, returnMode = 'image', showWarpedImage= True)
                splitBoard(img, 'image', 'store', True, name='Board' + str(i) + 'Square')
                i += 1
            else:
                print("board identification Failed")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        elif key == 'n':
            print('Data Collector Is Out...')
            break