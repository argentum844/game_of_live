import pygame
from forms import *


def draw_screen(field, screen, WIDTH, STEP):
    for i in range(WIDTH):
        for j in range(WIDTH):
            color = (0, 0, 0)
            pygame.draw.rect(screen, color, (STEP * j, STEP * i, STEP, STEP))
            if field[i][j] == 0:
                color = (255, 255, 255)
            else:
                color = (0, 255, 0)
            pygame.draw.rect(screen, color, (STEP * j + 1, STEP * i + 1, STEP - 1, STEP - 1))


def get_list1(WIDTH, STEP, field, form_to_insert):
    if form_to_insert == [[]]:
        is_form = False
    else:
        is_form = True
    pygame.init()
    screen = pygame.display.set_mode((WIDTH * STEP, WIDTH * STEP + 50))
    clock = pygame.time.Clock()
    draw_screen(field, screen, WIDTH, STEP)
    f1 = pygame.font.Font(None, 50)
    
    text = f1.render('Готово', 1, (255, 255, 255))
    place = text.get_rect(center=(WIDTH * STEP // 4, WIDTH * STEP + 25))
    screen.blit(text, place)

    text1 = f1.render('Формы', 1, (255, 255, 255))
    place = text1.get_rect(center=(WIDTH * STEP * 3 // 4, WIDTH * STEP + 25))
    screen.blit(text1, place)

    pygame.draw.line(screen, (255, 255, 255), [WIDTH * STEP // 2, WIDTH * STEP],
                     [WIDTH * STEP // 2, WIDTH * STEP + 50], 4)
    pygame.display.update()
    play = True
    f = False

    while play:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                return [True, [[]]]
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    f = True
                    x, y = i.pos
                    x = x // STEP
                    y = y // STEP
                    if y >= WIDTH:
                        if x <= WIDTH // 2:
                            play = False
                            f = False
                        else:
                            form_to_insert = get_form()
                            return [False, [field, form_to_insert]]
                    else:
                        pol = field[y][x]
                    if is_form:
                        if (len(form_to_insert) + x >= WIDTH or
                            len(form_to_insert[0]) + x >= WIDTH):
                            print("Некорректные координаты")
                        else:
                            field = insert_list(field, form_to_insert, x, y)
                        f = False
                        is_form = False
                        continue
                        
            if i.type == pygame.MOUSEBUTTONUP:
                f = False
        if f:
            x, y = i.pos
            x = x // STEP
            y = y // STEP
            if y >= WIDTH:
                continue
            if pol == 0:
                field[y][x] = 1
            else:
                field[y][x] = 0
        draw_screen(field, screen, WIDTH, STEP)
        pygame.display.update()
    pygame.quit()
    return [True, field]


def get_list(WIDTH, STEP, field):
    form_to_insert = [[]]
    while True:
        a, b = get_list1(WIDTH, STEP, field, form_to_insert)
        if a:
            return b
        else:
            field, form_to_insert = b
    


if __name__ == '__main__':
    field = [[0] * 50 for i in range(50)]
    a = get_list(50, 16, field)
