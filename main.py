import AI.AiHelpers.AiHelpers as ai
import ImageProcessing.ImageHelpers as im
import Sound.SoundHelper.SoundHelper as Sound
import ChessEngine.ChessHelpers.ChessHelpers as chess
import ChessEngine.WCRAchessEngine.ChessEngine as eng
import chess as C
import time

def print_board(newBoard):
	print('new board :')
	for i in range(8):
		print(newBoard.C[i])


#Sound.playSound('Call_Me_Ziko_Melody4Arab.Com.mp3',0.4)

prevBoard = chess.Board()
newBoard = chess.Board()


#newBoard, move = chess.compareBoards(newBoard, prevBoard, 'W')



#print('move: ',move)

board = C.Board()

while not board.is_game_over() :
	newBoard.setUC(chess.makeNewBoard(newBoard))
	newBoard, HumanMove = chess.compareBoards(newBoard, prevBoard, 'W')
	prevBoard.updateBoard(str(HumanMove),'W')
	print_board(newBoard)
	print('Your move is : ',HumanMove)
	eng.MakeMove(board,HumanMove)
	allMoves = board.legal_moves
	AiMove = eng.findBestMove(board,allMoves)
	newBoard.updateBoard( str(AiMove) , 'B')
	prevBoard.updateBoard(str(AiMove),'B')
	eng.MakeMove(board , AiMove )
	print(board)
	print('AI Move : ',AiMove)
	print('Make your move : ')
	time.sleep(20)
	print('10 secand lift.......')
	time.sleep(10)

game=eng.board_to_game(board)
print(game)
