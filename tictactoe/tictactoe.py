"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
]


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx = 0
    counto = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countx +=1
            if board[row][col] == O:
                counto +=1
    if countx > counto:
        return O
    else:
        return X
    

    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allposibleactions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                allposibleactions.add((row, col))

    return allposibleactions
    



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not valid action")
    
    row, col  = action

    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)

    return board_copy



def check_row(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False
   

def check_column(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False 

def check_firstdiagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    return False
def check_secondDiagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

            



            
        


def winner(board):
    
    if check_row(board, X) or check_column(board, X) or check_firstdiagonal(board, X) or check_secondDiagonal(board, X):
        return X
    elif check_row(board, O) or check_column(board, O) or check_firstdiagonal(board, O) or check_secondDiagonal(board, O):
        return O
    else:
        return None


def terminal(board):

    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True




def utility(board):
    
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0
    

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = +math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        

        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        

        return sorted(plays, key=lambda x: x[0])[0][1]
    

    




  