import pygame
button_size = 50


def insert_list(list1, list2, x, y):
    if len(list2) + y > len(list1) or len(list2[0]) + x > len(list1[0]) or x < 0 or y < 0:
        return list1
    for i in range(len(list2)):
        list1[y + i] = list1[y + i][:x] + list2[i] + list1[y + i][x + len(list2[i]):]
    return list1


def get_form():
    pygame.init()
    size_x, size_y = 400, len(forms) * button_size
    screen = pygame.display.set_mode((size_x, size_y))
    pygame.font.init()
    f1 = pygame.font.Font(None, 30)
    n = 0
    screen.fill((255, 255, 255))
    for i in forms:
        text = f1.render(i, 1, (0, 0, 0))
        place = text.get_rect(center=(size_x // 2, n * button_size + 25))
        screen.blit(text, place)
        pygame.draw.line(screen, (0, 0, 0), [0, n * button_size + 50],
                         [size_x, n * button_size + 50], 4)
        n += 1
    pygame.display.update()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return [[]]
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    x, y = i.pos
                    y = y // button_size
                    n = 0
                    for i in forms:
                        if n == y:
                            pygame.quit()
                            return forms[i]
                        n += 1


hup = [[0] * 24 + [1] + [0] * 11,
       [0] * 22 + [1, 0, 1] + [0] * 11,
       [0] * 12 + [1, 1] + [0] * 6 + [1, 1] + [0] * 12 + [1, 1],
       [0] * 11 + [1] + [0] * 3 + [1] + [0] * 4 + [1, 1] + [0] * 12 + [1, 1],
       [1, 1] + [0] * 8 + [1] + [0] * 5 + [1] + [0] * 3 + [1, 1] + [0] * 14,
       [1, 1] + [0] * 8 + [1, 0, 0, 0, 1, 0, 1, 1] + [0] * 4 + [1, 0, 1] + [0] * 11,
       [0] * 10 + [1] + [0] * 5 + [1] + [0] * 7 + [1] + [0] * 11,
       [0] * 11 + [1] + [0] * 3 + [1] + [0] * 20,
       [0] * 12 + [1, 1] + [0] * 22]

glider = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]

vertical_pendulum = [[1], [1], [1]]

horisontal_pendulum = [[1, 1, 1]]

square = [[1, 1], [1, 1]]
forms = {'Ружьё': hup,
         'Глайдер': glider,
         'Вертикальный маятник': vertical_pendulum,
         'Горизонтальный маятник': horisontal_pendulum,
         'Квадрат': square
         }

