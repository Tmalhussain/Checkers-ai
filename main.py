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

def menu():
    pg.font.init()
    clock = pg.time.Clock()
    run = True
    while run:
        WIN.fill((0,0,0))
        font = pg.font.Font(None, 50)
        text = font.render("Press 1 for AI mode, 2 for two-player mode", 1, (255, 255, 255))
        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    main(ai_mode=True)
                elif event.key == pg.K_2:
                    main(ai_mode=False)

        clock.tick(FPS)

def main(ai_mode):
    pg.font.init()
    run = True
    clock = pg.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        if game.turn == WHITE and ai_mode:
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
menu()
