"by mishari alhussain"
import pygame as pg
from checkers.constants import *
from checkers.game import *
from minimax.algorithm import minmax

FPS = 60

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pg.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minmax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)
        if game.winner():
            print(game.winner())
            run = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pg.quit()

main()