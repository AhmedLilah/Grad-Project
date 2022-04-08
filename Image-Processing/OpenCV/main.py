import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import glob

# # ASL = cv.imread('board_0001.jpeg',1)
# # cv.imshow('color',ASL)
# # cv.moveWindow('color',0,0)
# # hight, width, channels = ASL.shape
# # b,g,r = cv.split(ASL)
# # bgr_split= np.empty([hight,width*3,3],'uint8')
# # bgr_split[:,0:width]= cv.merge([b,b,b])
# # bgr_split[:,width:width*2]= cv.merge([g,g,g])
# # bgr_split[:,width*2:width*3]= cv.merge([r,r,r])
# # cv.imshow('bgr_split',bgr_split)
# # hsv = cv.cvtColor(ASL,cv.COLOR_BGR2HSV)
# # h,s,v = cv.split(hsv)
# # hsv_split = np.concatenate((h,s,v),axis=1)
# # cv.imshow('hsv_split',hsv_split)
# # gray= cv.cvtColor(ASL,cv.COLOR_BGR2GRAY)
# # cv.imwrite('ASL_gray.jpg',gray)
# # cv.imshow('ASL_gray',gray)

# # b = ASL[:,:,0]
# # g = ASL[:,:,1]
# # r = ASL[:,:,2]

# # bgra = cv.merge((b,g,r,g))
# # cv.imwrite('ASL_bgra.png',bgra)
# # cv.imshow('ASL_bgra',bgra)

# # g_blur = cv.GaussianBlur(ASL,(41,41),0)
# # cv.imshow('g_blur',g_blur)
# # cv.imwrite('g_blur.png',g_blur)

# # kernel = np.ones((5,5),'uint8')
# # dilate = cv.dilate(ASL,kernel,iterations=1)
# # erode = cv.erode(ASL,kernel,iterations=1)
# # cv.imshow('dilate',dilate)
# # cv.imshow('erode',erode)

# # ASL_half = cv.resize(ASL,(0,0), fx=0.5,fy=0.5)
# # ASL_stretch = cv.resize(ASL,(600,600),)
# # ASL_stretch_near = cv.resize(ASL,(600,600),interpolation=cv.INTER_NEAREST)
# # cv.imshow('ASL_half',ASL_half)
# # cv.imshow('ASL_stretch',ASL_stretch)
# # cv.imshow('ASL_stretch_near',ASL_stretch_near)
# # M = cv.getRotationMatrix2D((hight/2,width/2), -180,1)
# # rotated = cv.warpAffine(ASL,M,(ASL.shape[1],ASL.shape[0]))
# # cv.imshow('rotated',rotated)

# # # color = (0,255,0,0)
# # # radius = 20
# # # line_thikness = 3
# # # point = (0,0)

# # # def click(event,x,y,flags,param):
# # #     global point, pressed
# # #     if event == cv.EVENT_LBUTTONDOWN:
# # #         print('pressed',x,y)
# # #         point = (x,y)
# # #         color = (0,255,0,255)
# # #         radius = 3
# # #         if event == cv.EVENT_MOUSEMOVE:
# # #             print('moving',x,y)
# # #             point = (x,y)
# # #             color = (0,255,0,255)
# # #             radius = 3
# # #     elif event == cv.EVENT_LBUTTONUP:
# # #         print('not pressed',x,y)
# # #         point = (0,0)
# # #         radius = 0
    
# # # cv.namedWindow('frame')
# # # cv.setMouseCallback('frame',click)


# # # frame = np.ones_like(ASL)*255

# cap = cv.VideoCapture(0)
# while(True):
#     ret,frame = cap.read()
#     frame_edge = cv.Canny(frame,100,70)
#     frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     frame_thresh = cv.adaptiveThreshold(frame_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
#     face_detect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#     faces = face_detect.detectMultiScale(frame_gray,1.1,4)
#     for (x, y, w, h) in faces:
#         cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
#     cv.imshow('frame',frame)
#     # cv.imshow('frame_edge',frame_edge)
#     # cv.imshow('frame_thresh',frame_thresh)
#     ch = cv.waitKey(1)
#     if ch & 0xff == ord('q'):
#         break

# bw = cv.imread('sudoku.png',0)
# hight,width = bw.shape[0:2]
# cv.imshow('bw',bw)

# binary = np.zeros((hight,width,1),'uint8')

# thresh = 100

# for row in range(hight):
#     for col in range(width):
#         if bw[row][col] > thresh:
#             binary[row][col] = 255

# cv.imshow('binary', binary)

# ret,thresh = cv.threshold(bw,thresh,255,cv.THRESH_BINARY)
# adabtive_thresh = cv.adaptiveThreshold(bw,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)

# cv.imshow('thresh',thresh)
# cv.imshow('adabtive',adabtive_thresh)

# adabtive_thresh = cv.dilate(adabtive_thresh,(2,2),iterations=2)
# cv.imshow('adabtive_dilated',adabtive_thresh)


# faces = cv.imread('faces.jpeg')
# faces_hsv = cv.cvtColor(faces,cv.COLOR_BGR2HSV)
# faces_h = faces_hsv[:,:,[0]]
# faces_s = faces_hsv[:,:,[1]]
# faces_v = faces_hsv[:,:,[2]]

# faces_hsv_channels = np.concatenate((faces_h,faces_s,faces_v),axis=1)
# faces_hsv_channels = cv.resize(faces_hsv_channels,(0,0),fx=0.1,fy=0.1,)
# cv.imshow('faces_hsv_channels',faces_hsv_channels)

# ret, min_sat = cv.threshold(faces_s,40,255,cv.THRESH_BINARY)
# ret, max_hue = cv.threshold(faces_h,15,255,cv.THRESH_BINARY_INV)
# skin = cv.bitwise_and(min_sat,max_hue)
# min_sat = cv.resize(min_sat,(0,0),fx=0.2,fy=0.2,)
# max_hue = cv.resize(max_hue,(0,0),fx=0.2,fy=0.2,)
# skin = cv.resize(skin,(0,0),fx=0.2,fy=0.2,)
# cv.imshow('min_sat',min_sat)
# cv.imshow('max_hue',max_hue)
# cv.imshow('skin',skin)



# blob = cv.imread('detect_blob.png',1)
# gray = cv.cvtColor(blob,cv.COLOR_BGR2GRAY)
# thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
# cv.imshow('binary2',thresh)

# contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

# blob2 = blob.copy()
# index = -1 
# thikness = 4
# color = (255,0,255)

# cv.drawContours(blob2,contours,index,color,thikness)
# cv.imshow('contour', blob2)

# objects = np.zeros([blob.shape[0],blob.shape[1],3],'uint8')
# for c in contours:
#     cv.drawContours(objects,[c],-1,color,-1)

#     area = cv.contourArea(c)
#     perimeter = cv.arcLength(c,True)

#     M = cv.moments(c)
#     cx = int(M['m10']/M['m00'])
#     cy = int(M['m01']/M['m00'])

#     cv.circle(objects,(cx,cy),4,(0,0,255),-1)

#     print('area: {} perimeter: {}'.format(area,perimeter))

# cv.imshow("objects",objects)


# img = cv.imread('tomatoes.jpg',1)

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# res, thresh = cv.threshold(hsv[:,:,[0]],25,255, cv.THRESH_BINARY_INV )
# cv.imshow('tomatos',thresh)

# edges = cv.Canny(img,100,70)
# cv.imshow('canny',edges)

# fuzzy = cv.imread('fuzzy.png',1)
# fuzzy = cv.GaussianBlur(fuzzy,(5,5),sigmaX=5,sigmaY=5)
# cv.imshow('fuzzy_blur',fuzzy)

board = cv.imread('BoardTest3.png',1)
# board = cv.resize(board,(0,0),fx=0.5,fy=0.5)
cv.imshow('board',board)
gray = cv.cvtColor(board,cv.COLOR_BGR2GRAY)
thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,255,-25)
thresh2 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,255,-25)
thresh_erode = cv.erode(thresh,(5,5),iterations=1)
thresh_erode = cv.dilate(thresh,(5,5),iterations=1)
thresh_erode2 = cv.erode(thresh2,(5,5),iterations=1)
thresh_erode2 = cv.dilate(thresh2,(5,5),iterations=1)
cv.imshow('threh eroded',thresh_erode)
cv.imshow('threh eroded2',thresh_erode2)
# contours, hierarchy = cv.findContours(thresh_erode,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# contours2, hierarchy2 = cv.findContours(thresh_erode2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# board2 = board.copy()
# board3 = board.copy()
# index = -1 
# thikness = 2
# color = (255,255,0)
# color2 = (0,255,255)

# big_contours  =[]
# big_contours2  =[]
# for c in contours:
#     if cv.contourArea(c) > 100 and cv.contourArea(c) < 24000:
#         big_contours.append(c)
# for c in contours2:
#     if cv.contourArea(c) > 100 and cv.contourArea(c) < 10000:
#         big_contours2.append(c)

# cv.drawContours(board2,big_contours,index,color,thikness)
# cv.drawContours(board3,big_contours2,index,color2,thikness)
# cv.imshow('board_contour',board2 )
# cv.imshow('board_contour3',board3 )


#****************************************************************
# Load the image
# img = cv.imread('board_0001.jpeg') 
 
# Create a copy of the image
# img_copy = np.copy(img)
 
# Convert to RGB so as to display via matplotlib
# Using Matplotlib we can easily find the coordinates
# of the 4 points that is essential for finding the 
# transformation matrix
# img_copy = cv.cvtColor(img_copy,cv.COLOR_BGR2RGB)
 
# plt.imshow(img_copy)

# # All points are in format [cols, rows]
# pt_A = [30, 250]
# pt_B = [30, 1380]
# pt_C = [900, 1220]
# pt_D = [900, 395]
# # Here, I have used L2 norm. You can use L1 also.
# width_AD = np.sqrt(((pt_A[0] - pt_D[0]) ** 2) + ((pt_A[1] - pt_D[1]) ** 2))
# width_BC = np.sqrt(((pt_B[0] - pt_C[0]) ** 2) + ((pt_B[1] - pt_C[1]) ** 2))
# maxWidth = max(int(width_AD), int(width_BC))
# height_AB = np.sqrt(((pt_A[0] - pt_B[0]) ** 2) + ((pt_A[1] - pt_B[1]) ** 2))
# height_CD = np.sqrt(((pt_C[0] - pt_D[0]) ** 2) + ((pt_C[1] - pt_D[1]) ** 2))
# maxHeight = max(int(height_AB), int(height_CD))


# input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
# output_pts = np.float32([[0, 0],
#                         [0, maxHeight - 1],
#                         [maxWidth - 1, maxHeight - 1],
#                         [maxWidth - 1, 0]])
# # Compute the perspective transform M
# M = cv.getPerspectiveTransform(input_pts,output_pts)
# out = cv.warpPerspective(img,M,(maxWidth, maxHeight),flags=cv.INTER_LINEAR)
# out =  cv.resize(out,(0,0),fx = 0.7, fy=0.7)
# img =  cv.resize(img,(0,0),fx = 0.7, fy=0.7)
# cv.imshow('warp_prespective_original',img)
# cv.imshow('warp_prespective',out)

# nline = 6
# ncol = 6

# img = cv.imread(glob.glob('board_0001.jpeg')[0])

# ## termination criteria
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# ## processing
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Find the chessboard corners
# ret, corners = cv.findChessboardCorners(gray, (nline, ncol), None)
# corners2 = cv.cornerSubPix(gray, corners, (6, 6), (-1, -1), criteria)


# cap.release()
cv.waitKey(0)
cv.destroyAllWindows()

