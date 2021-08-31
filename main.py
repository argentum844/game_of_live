from players_list import get_list, draw_screen
from board import Board
import pygame
from forms import *


WIDTH, STEP = 30, 16


def main(field):
    fps = 4
    pygame.init()
    field = get_list(WIDTH, STEP, field)
    if field == [[]]:
        pygame.quit()
        return [False, [[]]]
    board = Board(field, WIDTH)
    screen = pygame.display.set_mode((WIDTH * STEP, WIDTH * STEP + 50))
    clock = pygame.time.Clock()
    pygame.font.init()
    
    f1 = pygame.font.Font(None, 50)
    
    text = f1.render('Заново', 1, (255, 255, 255))
    place = text.get_rect(center=(WIDTH * STEP // 4, WIDTH * STEP + 25))
    screen.blit(text, place)
    
    text1 = f1.render('Редактировать', 1, (255, 255, 255))
    place = text1.get_rect(center=(WIDTH * STEP * 3 // 4, WIDTH * STEP + 25))
    screen.blit(text1, place)

    pygame.draw.line(screen, (255, 255, 255), [WIDTH * STEP // 2, WIDTH * STEP],
                     [WIDTH * STEP // 2, WIDTH * STEP + 50], 4)
                                               
    
    pygame.display.update()
    play = True

    while play:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                return [False, []]
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    x, y = i.pos
                    x = x // STEP
                    y = y // STEP
                    if y >= WIDTH:
                        if x <= WIDTH // 2:
                            return [True, [[0] * WIDTH for i in range(WIDTH)]]
                        return [True, board.field]
                if i.button == 4:
                    fps += 1
                if i.button == 5:
                    fps -= 1
        if fps <= 0:
            fps = 0
            continue
        board.update()
        draw_screen(board.field, screen, WIDTH, STEP)
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    field = [[0] * WIDTH for i in range(WIDTH)]
    #field = insert_list(field, hup, 0, 0)
    while True:
        a, field = main(field)
        if not a:
            break
