import pygame
import sys
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Война вирусов")


def rules():
    def blit_text(surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    text = "1. Каждый ход состоит из трёх отдельных последовательных ходов." \
           "Каждый ход является либо размножением, либо убиванием. " \
           "\n2.Размножение — это выставление своего символа в любую доступную пустую клетку доски, " \
           "убивание — объявление убитым некоторого чужого символа, который находится на доступной клетке." \
           "\n3. В начале игры крестики начинают ход на a1. Точно также нолики начинают на k10." \
           "\n4. Клетка считается доступной, если она либо непосредственно соприкасается с живым знаком, либо через цепочку убитых знаков" \
           "\nЗапрещается:" \
           "\nСтавить свой символ в уже занятую клетку." \
           "\nУбивать уже убитые символы противника." \
           "\nНажмите 'ESC' чтобы выйти"

    font = pygame.font.SysFont('comicsansms', 20)
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                    start_menu()

        surface.fill(pygame.Color('white'))
        blit_text(surface, text, (20, 20), font)
        pygame.display.update()


def start_the_game():
    size_block = 40
    margin = 10
    screen = pygame.display.set_mode((510, 510))
    loop = True
    green = (0, 255, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    mas = [[0] * 10 for _ in range(10)]
    query = 0
    step = 'x'
    step_converter = {'x': 's', 'o': 'z'}
    startX = True
    startO = True

    def nigger(row, column):
        # Левый верхний угол
        if _is_valid([row - 1, column - 1]):
            if mas[row - 1][column - 1] != 0 and (mas[row - 1][column - 1] == step
                                                  or mas[row - 1][column - 1] == step_converter[step]):
                return True
        # Центр верх
        if _is_valid([row - 1, column]):
            if mas[row - 1][column] != 0 and (mas[row - 1][column] == step
                                              or mas[row - 1][column] == step_converter[step]):
                return True
        # Правый верхний угол
        if _is_valid([row - 1, column + 1]):
            if mas[row - 1][column + 1] != 0 and (mas[row - 1][column + 1] == step
                                                  or mas[row - 1][column + 1] == step_converter[step]):
                return True
        # Центр право
        if _is_valid([row, column + 1]):
            if mas[row][column + 1] != 0 and (mas[row][column + 1] == step
                                              or mas[row][column + 1] == step_converter[step]):
                return True
        # Правый нижний угол
        if _is_valid([row + 1, column + 1]):
            if mas[row + 1][column + 1] != 0 and (mas[row + 1][column + 1] == step
                                                  or mas[row + 1][column + 1] == step_converter[step]):
                return True
        # Центр низ
        if _is_valid([row + 1, column]):
            if mas[row + 1][column] != 0 and (mas[row + 1][column] == step
                                              or mas[row + 1][column] == step_converter[step]):
                return True
        # Левый нижний угол
        if _is_valid([row + 1, column - 1]):
            if mas[row + 1][column - 1] != 0 and (mas[row + 1][column - 1] == step
                                                  or mas[row + 1][column - 1] == step_converter[step]):
                return True
        # Центр лево
        if _is_valid([row, column - 1]):
            if mas[row][column - 1] != 0 and (mas[row][column - 1] == step
                                              or mas[row][column - 1] == step_converter[step]):
                return True
        return False

    def has_free_cells():
        for current_row in mas:
            if 0 in current_row: return True
        return False

    while loop:
        if not has_free_cells():
            pass
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    print(f'x={x_mouse} y={y_mouse}')
                    col = x_mouse // (margin + size_block + 1)
                    row = y_mouse // (margin + size_block + 1)
                    if startX == True:
                        if step == 'x' and col == 0 and row == 0:
                            mas[row][col] = 'x'
                            query += 1
                            startX = False
                    if startO == True:
                        if step == 'o' and col == 9 and row == 9:
                            mas[row][col] = 'o'
                            query += 1
                            startO = False

                    if startX == False:
                        if step == 'x':
                            if mas[row][col] == 0 and nigger(row, col):
                                mas[row][col] = 'x'
                                query += 1
                            if mas[row][col] == 'o' and nigger(row, col):
                                mas[row][col] = 's'  # убитый o
                                query += 1
                    if startO == False:
                        if step == 'o':
                            if mas[row][col] == 0 and nigger(row, col):
                                mas[row][col] = 'o'
                                query += 1
                            if mas[row][col] == 'x' and nigger(row, col):
                                mas[row][col] = 'z'  # убитый x
                                query += 1
                    if query == 3:
                        if step == 'x':
                            step = 'o'
                        elif step == 'o':
                            step = 'x'
                        query = 0

            for row in range(10):
                for col in range(10):
                    if mas[row][col] == 'x':
                        color = red
                    elif mas[row][col] == 'o':
                        color = green
                    elif mas[row][col] == 'z':
                        color = red
                    elif mas[row][col] == 's':
                        color = blue
                    else:
                        color = white
                    x = col * size_block + (col + 1) * margin
                    y = row * size_block + (row + 1) * margin
                    pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                    if color == red:
                        if mas[row][col] != 'z':
                            pygame.draw.line(screen, white, (x, y), (x + size_block, y + size_block), 3)
                            pygame.draw.line(screen, white, (x + size_block, y), (x, y + size_block), 3)
                        else:
                            pygame.draw.line(screen, white, (x, y), (x + size_block, y + size_block), 3)
                            pygame.draw.line(screen, white, (x + size_block, y), (x, y + size_block), 3)
                            pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2),
                                               size_block // 2 - 3, 3)
                    elif color == green and mas[row][col] != 's':
                        pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2),
                                           size_block // 2 - 3,
                                           3)
            pygame.display.update()


def _is_valid(value):
    if 9 >= value[0] >= 0 and 9 >= value[1] >= 0:
        return True
    return False


def start_menu():
    menu = pygame_menu.Menu('Приветсвуем', 600, 600,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Играть', start_the_game)
    menu.add.button('Правила', rules)
    menu.add.button('Выйти', pygame_menu.events.EXIT)
    menu.mainloop(surface)

start_menu()
