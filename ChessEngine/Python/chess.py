def mk_board():
    print('in mk_board')
    board = [['' for i in range(8)] for j in range(8) ]
    for i in range(8):
        for j in range(8):
            if (not((i+j)%2)):
                board[i][j] = '*'
            if ((i+j)%2):
                board[i][j] = '.'
    for i in range(8):
        board[1][i] = 'B'
        board[6][i] = 'B'
    return board

def prnt_board(board):
    print('in prnt_board')
    for i in range(8):
        for j in range(8):
            print(board[i][j],end='\t  ')
        print(end='\n\n\n\n')

def slctd(board):
    print('in slctd')
    for i in range(8):
        for j in range(8):
                if board[i][j] == 'BS':
                    sho_mov(board,i,j)

def slct(board,i,j):
    print('in slct')
    board[i][j] = 'BS'


def sho_mov(board,k,l):
    print('in sho_mov')
    mov_board = board
    if k == 1:
        mov_board[k+2][l] = 'AM'
        mov_board[k+1][l] = 'AM'
    else:
        mov_board[k+1][l] = 'AM'
    prnt_board(mov_board)


board = mk_board()

prnt_board(board)

slct(board,1,2)

slctd(board)