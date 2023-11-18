from copy import deepcopy
import pygame as pg
import time
RED=(255,0,0)
WHITE=(255,255,255)


def iterative_deepening(position, max_depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
    best_move = None
    for depth in range(1, max_depth + 1):
        start = time.time()
        try:
            eval, move = minimax(position, depth, max_player, game, alpha, beta)
            best_move = move
        except TimeoutError:
            break
        end = time.time()
        if end - start > 1:  
            break
    return best_move

def minmax(position, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or position.winner() != None:
        return position.eval(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evalu = minmax(move, depth - 1, False, game, alpha, beta)[0]
            maxEval = max(maxEval, evalu)
            if maxEval == evalu:
                best_move = move
            alpha = max(alpha, evalu)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evalu = minmax(move, depth - 1, True, game, alpha, beta)[0]
            minEval = min(minEval, evalu)
            if minEval == evalu:
                best_move = move
            beta = min(beta, evalu)
            if beta <= alpha:
                break
        return minEval, best_move
    

def simulate_move(piece,move,board,game,skip):
    board.move(piece,move[0],move[1])
    if skip:
        board.remove(skip)
    return board

def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves
