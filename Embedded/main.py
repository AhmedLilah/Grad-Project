import AI.AiHelpers.AiHelpers as ai
import ImageProcessing.ImageHelpers as im
import Sound.SoundHelper.SoundHelper as Sound
import ChessEngine.ChessHelpers.ChessHelpers as chess
import ChessEngine.WCRAchessEngine.ChessEngine as eng
import Embedded.i2c as em
import Embedded.ArduinoCom as rc
import chess as C   
import time

time_limit = 3 

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
color = ''
mode = ''
modes = ['online', 'offline']
difficulties =['easy', 'hard']
while(mode != "1" and mode != "2"):
	em.writedata("0000o")
	mode = rc.getArdunioResponse()
	print("you are playing " + modes[int(mode)-1])

if mode == '2':
	difficulty = rc.getArdunioResponse()
	print("you are playing " + difficulties[int(difficulty)-1])
	if difficulty == '2' :
		engine = eng.SetupEngine9()

while(color != "1" and color != "2"):
	em.writedata("0000x")
	color = rc.getArdunioResponse()
	print("your color is" + color)

if color == '2':
	print('start the game')
	while not board.is_game_over() :
		newBoard.setUC(chess.makeNewBoard(newBoard))
		newBoard, HumanMove = chess.compareBoards(newBoard, prevBoard, 'W')
		prevBoard.updateBoard(HumanMove,'W')
		print_board(newBoard)
		print('Your move is : ',HumanMove)
		eng.MakeMove(board,HumanMove)	
		allMoves = board.legal_moves
 		# print("the engine is thinking.....")
		AiMove , armMove  = eng.findBestMove(board,allMoves)
		print('this is armMove: ',armMove)
		newBoard.updateBoard( str(AiMove) , 'B')
		prevBoard.updateBoard(str(AiMove),'B')
		eng.MakeMove(board , AiMove )
		print(board)
		print('AI Move : ',AiMove)
		em.writeData(armMove)
		print('Make your move : ')
		time.sleep(20)
		print('10 secand lift.......')
		time.sleep(10)
elif color == '1':
	print("the engine is thinking....") 
	while not board.is_game_over():
		firstTurn = True
		allMoves = board.legal_moves
		AiMove , armMove = eng.findBestMove(board,allMoves)
		print('this is armMove: ',armMove)
		newBoard.updateBoard( str(AiMove) , 'w')
		prevBoard.updateBoard(str(AiMove),'w')
		eng.MakeMove(board , AiMove )
		print(board)
		print('AI Move : ',AiMove)
		em.writeData(armMove)
		print('Make your move : ')
		time.sleep(20)
		print('30 secand lift.......')
		time.sleep(20)
		newBoard.setUC(chess.makeNewBoard(newBoard))
		newBoard, HumanMove = chess.compareBoards(newBoard, prevBoard, 'B')
		prevBoard.updateBoard(str(HumanMove),'B')
		print_board(newBoard)
		print('Your move is : ',HumanMove)
		eng.MakeMove(board,HumanMove)
		firstTurn = False
else:
	print("SOMETHING WENTWRONG")




game=eng.board_to_game(board)
print(game)






























'''

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
'''