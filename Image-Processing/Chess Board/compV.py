import cv2
import numpy as np
from BoardClass import Board

ret = []

def CameraInit(im) :
    top_left , top_right , bottom_left , bottom_right = findpoints(im)
    pts = np.array( [top_left, top_right, bottom_left, bottom_right], dtype="float32")
    print("pts: ", pts)
    return pts


def FindColor ( bgr ) :

    # if ( bgr[0] * 0.0722 + bgr[1] * 0.7152 +bgr[2] * 0.2126 ) > 225 and :     
    #  R*0.2126+ G*0.7152+ B*0.0722
    if (int(bgr[0])+ int(bgr[1])+int(bgr[2])) >600:
        color = 'W'
        print('white')

    elif (int(bgr[0])+ int(bgr[1])+int(bgr[2]))<400:
        color = 'B'
        print('black')

    #If the color is not black or white , it set to ’-’ and not used .
    else :
        color = '-'
        print('No color')
    return color



def findpoints( image ) :

    # This is a termination criteria
    criteria = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER ,30 , 0.001)
    img = cv2.imread (image) # Reads the image
    gray = cv2.cvtColor (img ,cv2.COLOR_BGR2GRAY ) # Converts the image to grayscale .
    ret = False
    
    # Find the chessboard inner corners
    ret , corners = cv2.findChessboardCorners( gray , (7 ,7) )
    #print('ret :',ret)
    #print('cornals: ' , corners)
    
    # If corners are found , object and image points are added .
    # This section is not needed but can provide futher understanding of the program
    # as it displays the identified chessboard corners on top of the image .
    if ret == True :
        cv2.cornerSubPix( gray , corners , (11 ,11) , ( -1 , -1) , criteria )
        cv2.drawChessboardCorners( img , (7 ,7) , corners , ret )
        cv2.imshow('img' , img )
        cv2.imwrite('imgcorners.jpg ', img )
        cv2.waitKey(0)
    cv2.destroyAllWindows ()

    Top_Left_x=2* corners[0][0][0] - corners[8][0][0]
    Top_Left_y = 2* corners[0][0][1] - corners[8][0][1]
    Top_Right_x = 2* corners[6][0][0] - corners[12][0][0]
    Top_Right_y = 2* corners[6][0][1] - corners[12][0][1]
    Bottom_Left_x = 2* corners[42][0][0] - corners[36][0][0]
    Bottom_Left_y = 2* corners[42][0][1] - corners[36][0][1]
    Bottom_Right_x = 2* corners[48][0][0] - corners[40][0][0]
    Bottom_Right_y = 2* corners[48][0][1] - corners[40][0][1]
    Bottom_Left = ( Bottom_Left_x , Bottom_Left_y )
    Bottom_Right = ( Bottom_Right_x , Bottom_Right_y )
    Top_Left = ( Top_Left_x , Top_Left_y )
    Top_Right = ( Top_Right_x , Top_Right_y )

    return Top_Left , Top_Right , Bottom_Left , Bottom_Right



def CompareBoards( PrevBoard  ,PATH ) :
    Picture = cv2.imread (PATH, 1) #Opening the picture of chessboard . Location is hardcoded
    Width , Height , channels = Picture.shape # Retrieving the size of the picture
    Files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    Ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
    Kord = [1/16 , 3/16 , 5/16 , 7/16 , 9/16 , 11/16 , 13/16 , 15/16]
    XKord = [ x * Width for x in Kord ] 
    YKord = [ x * Height for x in Kord ]
    NewBoard = Board()
    CountX = 0
    for x in XKord :

        CountY = 0
        for y in YKord :

            # Check what color is in the pixels by retrieving the rgb - values .
            # Since there is a screw fastened at the top of each piece , there is a chance that the pixel in the center of each square contains the screw
            #and therefore is inaccurately classed as an empty square , since it isn ’t classed as blue nor red. Therefore two more pixels along the center
            #of the square ’s Y- axis is analysed if no colors are found .

            Color = FindColor ( Picture [int( x ) , int( y ) ])
            if Color != 'B' and Color != 'W':
                Color = FindColor ( Picture [int( x ) +int ((1/32) * Width ) , int ( y ) +int ((1/32) * Height ) ])
                if Color != 'B' and Color != 'W':
                    Color = FindColor ( Picture [int( x ) -int ((1/32) * Width) , int( y ) -int ((1/32) * Height ) ])
            if Color == 'B' or Color == 'W':
                NewBoard.updateUC ( CountX , CountY , Color ) # Update the board with the correct colors

            CountY += 1
        CountX += 1

    # Print the unclassified board . Good tool to see if the color recognition is working as intended .
    # for q in NewBoard .UC:
    # print (q)

    NewRank = '1'
    NewFile = 'a'

    for i in range (0 ,8) :
        for j in range (0 ,8) :
            # If a square now holds a piece it didnt before , this is where a piece has moved .
            if NewBoard.UC [ i ][ j ] == 'B' and PrevBoard.UC [ i ][ j ] != 'B':
                NewRank = Ranks [ i ]
                NewFile = Files [ j ]

            # If a square now doesn ’t hold a piece aand it previously did , this is where a piece has moved from.
            if NewBoard.UC [ i ][ j ] != 'B' and PrevBoard.UC [ i ][ j ] == 'B':
                OldRank = Ranks [ i ]
                OldFile = Files [ j ]

            # for debuging code  
            else:
                NewRank = '1'
                NewFile = 'a'


            # Update the board using the new and old ranks and files .
            PrevBoard.updateCBoard ( Ranks.index ( NewRank ) , Files.index ( NewFile ), Ranks.index ( OldRank ) , Files.index ( OldFile ) )
            
            # Update the unclassified board .
            PrevBoard.UC = NewBoard . UC

    return PrevBoard



def NewImage( pts,path , npath) :
    img2 = path
    img = cv2.imread( img2 ) # Reads the image so that it may be processed
    Warped = four_point_transform( img , pts ) # Using a four point transform to warp the image .

    cv2.imwrite (npath, Warped ) #Saving the warped image

    return npath

def four_point_transform ( image , pts ) :

    Rect = order_points( pts )
    ( Topleft , TopRight , BottomRight , BottomLeft ) = Rect

    # Calculate the width of the image .
    # Maximum distance between top - right and top - left or bottom - left and bottom - right y- coordinates .
    widthA = np.sqrt ((( BottomRight [0] - BottomLeft [0]) ** 2) + ((BottomRight [1] - BottomLeft [1]) ** 2) )
    widthB = np.sqrt ((( TopRight [0] - Topleft [0]) ** 2) + (( TopRight[1] - Topleft [1]) ** 2) )
    maxWidth = max(int( widthA ) , int( widthB ) )

    # Calculate the height of the image .
    # Maximum distance between top - right and bottom - right or top - left and bottom - left y- coordinates .
    heightA = np.sqrt ((( TopRight [0] - BottomRight [0]) ** 2) + ((
    TopRight [1] - BottomRight [1]) ** 2) )
    heightB = np.sqrt ((( Topleft [0] - BottomLeft [0]) ** 2) + (( Topleft[1] - BottomLeft [1]) ** 2) )
    maxHeight = max(int( heightA ) , int( heightB ) )

    # Create an array with the desired image structure .
    dst = np.array ([[0 , 0] ,[ maxWidth - 1 , 0] ,[ maxWidth - 1 , maxHeight - 1] ,[0 , maxHeight - 1]] , dtype = "float32")

    # Using cv2. getPerspectiveTransform we get the correct perspective transform .
    # Input is the location of the corners on the original image , and their destination .
    M = cv2.getPerspectiveTransform ( Rect , dst )
    
    Warped = cv2.warpPerspective ( image , M , ( maxWidth , maxHeight ) )
    
    return Warped


def order_points(pts ) :
    # Initialise a list . The entries will be ordered so that theentries will be:
    #[Top left , Top right , Bottom right , Bottom Left ]
    #The origin is in the top left corner , hence the top left corner will have the
    # smallest sum , the bottom right the largest sum , the top right the smallest difference
    # from the horizontal axis and the bottom left the largest difference from the same .
    Rect = np.zeros ((4 , 2) , dtype = "float32")
    s = pts.sum( axis = 1)
    Rect [0] = pts [np.argmin (s)]
    Rect [2] = pts [np.argmax (s)]
    diff = np.diff ( pts , axis = 1)
    Rect [1] = pts [np.argmin (diff)]
    Rect [3] = pts [np.argmax (diff)]
    # Return the coordinates .
    return Rect


def Initiate() :
    ChessBoard = Board()
    ChessBoard.firstUC()
    return ChessBoard


board=Initiate()
print('***********************************************************************')
print(board.UC)
print(board.C)
print('***********************************************************************')

PTS=CameraInit(r'C:\Users\sabry\Desktop\Chess Board\chpic.jpg')
NewImage(PTS,r'C:\Users\sabry\Desktop\Chess Board\chpic.jpg'  ,   r'C:\Users\sabry\Desktop\Chess Board\newimg000.jpg')

board=CompareBoards( board  ,r'C:\Users\sabry\Desktop\Chess Board\newimg000.jpg' )
print('***********************************************************************')
print(board.UC)
print('***********************************************************************')
print(board.C)
print('***********************************************************************')
