import math
import random
import numpy as np

class Tic_Tac_Toe:
    def __init__(self):
        self.dim = 0
        self.AI = None
        self.human = None         
    
    def set_players(self, player, n):
        self.dim = n
        self.AI = player
        if self.AI=='X':
            self.human = 'O'
        elif self.AI=='O':
            self.human = 'X'
            
    def get_human(self):
        return self.human
    
    def checker(self, board1):
        dim = int(math.sqrt(len(board1)))
        board = np.array([0]*len(board1))
        for i in range(len(board1)):
            if board1[i]=='X':
                board[i] = 1
            elif board1[i]=='O':
                board[i] = 0
            elif board1[i]==' ':
                board[i] = -10
        board = board.reshape(dim, dim)
        row = 0
        daigonal2 = 0
        daigonal1 = np.trace(board)
        for i in range(0, len(board[0])):
            daigonal2 += board[i][len(board[0])-i-1]
        data = list()
        data.append(daigonal1)
        data.append(daigonal2)
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                row += board[i][j]
            data.append(row)
            row = 0
        board = board.T
        row = 0
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                row += board[i][j]
            data.append(row)
            row = 0
        sum1 = dim
        sum2 = 0
        if sum1 in data:
            return 'X'
        elif sum2 in data:
            return 'O'
        return '-'

    def alpha_beta(self, board, player, alpha=-np.inf, beta=np.inf):
        winner = self.checker(board)
        if winner==self.AI:
            return 5
        elif winner==self.human:
            return -5
        elif ' ' not in board:
            return 0
        
        if player==self.AI:          #Alpha
            best = -np.inf
            for i in range(len(board)):
                if board[i]==' ':
                    board[i] = self.AI
                    val = self.alpha_beta(board, self.human, alpha, beta)
                    board[i] = ' '
                    best = max(val, best)
                    alpha = max(best, alpha)
                    if alpha >= beta:
                        break
        elif player==self.human:     #Beta
            best = np.inf
            for i in range(len(board)):
                if board[i]==' ':
                    board[i] = self.human
                    val = self.alpha_beta(board, self.AI, alpha, beta)
                    board[i] = ' '
                    best = min(val, best)
                    beta = min(best, beta)
                    if alpha >= beta:
                        break
        return best
        
    def filled_space(self, board):
        count = 0
        for i in board:
            if i!=' ':
                count+=1
        return count
        
    def rand_move(self, board):
        empty_slotes = list()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==' ':
                    empty_slotes.append((i,j))
        return random.choice(empty_slotes)

            
def Agent(Currentboard, n, AI):
    game = Tic_Tac_Toe()
    game.set_players(AI, n)
    board = np.array(Currentboard)
    free = game.filled_space(board.reshape(-1))
    if len(set(board.reshape(-1)))==1:
        board[0][0] = AI
        return board
    elif free<4 and n==4:
        move = game.rand_move(board)
        board[move] = AI
        return board
    elif free<7 and n==5:
        move = game.rand_move(board)
        board[move] = AI
        return board
    elif free<9 and n==6:
        move = game.rand_move(board)
        board[move] = AI
        return board
    move = None
    score = -np.inf
    for i in range(n):
        for j in range(n):
            if board[i][j]==' ':
                board[i][j] = AI
                bestscore = game.alpha_beta(board.reshape(-1), game.get_human())
                board[i][j] = ' '
                if bestscore>score:
                    score = bestscore
                    move = (i,j)
    board[move] = AI
    return board

def end(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==' ':
                return True
    return False


no = int(input('Enter Value of n to make nxn Board : '))

game1 = Tic_Tac_Toe()
board = np.array([[' ']*no]*no)
print(board)

print(' ')
print('Enter Value from 1 to ', no*no)
print(' ')

for i in range(9):
    if end(board):
        check = game1.checker(board.reshape(-1))
        if check=='X':
            print('X won')
            break
        elif check=='O':
            print('O won')
            break
        player1 = input('Enter position : ')
        player1 = int(player1)
        board = board.reshape(-1)
        board[player1-1] = 'O'
        board = board.reshape(no,no)
        print('Human : ')
        print(board)
        print('')
        
    if end(board):
        check = game1.checker(board.reshape(-1))
        if check=='X':
            print('X won')
            break
        elif check=='O':
            print('O won')
            break
        board = Agent(board, no, 'X')
        print('Agent: ')
        print(board)
        print('')
