import numpy as np 
import cv2



img = cv2.imread("newimg000.jpg")

cells = []
counter = 0 
for i in range(1,9):
    x = int(i/8 * img.shape[0])
    x_1 = int((i-1)/8 * img.shape[0])
    for j in range(1,9):
        y = int(j/8 * img.shape[1])
        y_1 = int((j-1)/8 * img.shape[0])

        cells.append(np.array(img[x_1:x,y_1:y]))

        cropedImage = np.array(img[x_1:x,y_1:y])
        resizedImage = cv2.resize(cropedImage,(400,400))
        cv2.imshow("crop"+str(counter),resizedImage)
        cv2.imwrite("croped"+str(counter)+'.jpg' , cropedImage )
        counter +=1

cv2.waitKey(0)
cv2.destroyAllWindows()
