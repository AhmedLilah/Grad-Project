import numpy as np
import sys
sys.path.insert(0,'../../AI-ML')
import AiHelpers as ai

sys.path.insert(0,'../../Image-Processing')
import ImageHelpers as im
class Board:    
    def __init__(self):
        self.C =[
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        
        self.UC=[
            ["B", "B", "B", "B", "B", "B", "B", "B"],
            ["B", "B", "B", "B", "B", "B", "B", "B"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
        ]

    def updateBoard ( self, NewRank, NewFile, OldRank, OldFile, playerColor):
        self.UC [ NewRank ][ NewFile ] = playerColor
        self.UC [ OldRank ][ OldFile ] = '1'
        self.C [NewRank][NewFile] = self.C [ OldRank ][ OldFile ]
        self.C [OldRank][OldFile] = '1'


def makeNewBoard(newBoard):
    colorDict = {0:'1', 1:'W', 2:'B'}
    board = im.catureAiSequence()
    board = np.array(board)
    board = np.reshape(board, (8,8))
    for i in range(8):
        for j in range(8):
            newBoard.UC[i][j] = colorDict[ai.runAiModel(board[i][j])]
    return newBoard

def CompareBoards( newBoard, prevBoard, playerColor = 'B') :

    Files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    Ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
   
    newBoard = Board()

    # Print the unclassified board . Good tool to see if the color recognition is working as intended .
    # for q in newBoard .UC:
    # print (q)
    for i in range (0 ,8) :
        for j in range (0 ,8) :
            #If a square now holds a piece it didnt before , this is where a piece has moved .
            if newBoard[i][j] == playerColor and prevBoard[i][j] != playerColor:
                NewRank = Ranks [i]
                NewFile = Files [j]

            #If a square now doesn ’t hold a piece and it previously did , this is where a piece has moved from.
            if newBoard.UC [i][j] != playerColor and prevBoard.UC [ i ][ j ] == playerColor:
                OldRank = Ranks [i]
                OldFile = Files [j]

    newBoard.updateBoard( Ranks.index(NewRank), Files.index(NewFile), Ranks.index(OldRank), Files.index (OldFile), playerColor)
    return newBoard, [NewFile, NewRank, OldFile, OldRank]
