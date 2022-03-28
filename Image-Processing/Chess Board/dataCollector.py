from ImageHelpers import *

if __name__ == '__main__':
    img = captureImage(showImage= True)
    ret , pts = findPoints('chpic.jpg', inputMode= 'path', showPoints= True)
    #img = cv2.imread("chpic.jpg")
    if ret:
        img = fourPointsTransform(img, pts, returnMode = 'image', showWarpedImage= True)
        splitBoard(img, 'image', 'store', True, name='test')
