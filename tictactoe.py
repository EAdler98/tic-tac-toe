"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xcount += 1
            elif board[i][j] == O:
                Ocount += 1
    if Xcount == Ocount:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionsSet.add((i, j))
    return actionsSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    modboard = copy.deepcopy(board)
    modboard[action[0]][action[1]] = player(board)
    return modboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == O or board[0][i] == board[1][i] == board[2][i] == O:
            return O
        if board[i][0] == board[i][1] == board[i][2] == X or board[0][i] == board[1][i] == board[2][i] == X:
            return X
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal = None
    if terminal(board):
        return None
    v = None
    if player(board) == X:
        v = -2
        for action in actions(board):
            temp = minimaxA(result(board, action), 2, -2)
            if temp > v:
                v = temp
                optimal = action
    if player(board) == O:
        v = 2
        for action in actions(board):
            temp = minimaxA(result(board, action), 2, -2)
            if temp < v:
                v = temp
                optimal = action
    return optimal


def minimaxA(board, minv, maxv):
    if terminal(board):
        return utility(board)
    v = None
    if player(board) == X:
        v = -2
        for action in actions(board):
            if terminal(result(board, action)):
                return utility(result(board, action))
            temp = minimaxA(result(board, action), 2, -2)
            maxv = max(maxv, temp)
            if minv <= maxv:
                break
        return maxv
    if player(board) == O:
        v = 2
        for action in actions(board):
            if terminal(result(board, action)):
                return utility(result(board, action))
            temp = minimaxA(result(board, action), 2, -2)
            minv = min(minv, temp)
            if minv <= maxv:
                break
        return minv
