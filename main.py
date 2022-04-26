import AI.AiHelpers as ai
import ChessEngine.ChessHelpers.ChessHelpers as chess
import ImageProcessing.ChessBoard.ImageHelpers as im

prevBoard = chess.Board()
newBoard = chess.Board()

newBoard = chess.makeNewBoard(newBoard)

newBoard, move = chess.compareBoard(newBoard, prevBoard, 'B')

print("prevBoard: \n", prevBoard.C)
print("newBoard: \n", newBoard.C)