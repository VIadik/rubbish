import pygame
import random
from collections import deque

HEIGHT = 20
WIDTH = 10

used = [[False for i in range(WIDTH)] for j in range(HEIGHT)]

# the first value means that there is a wall at the bottom, and the second on the right
walls = [[[True, True] for i in range(WIDTH)] for j in range(HEIGHT)]


def make_labirint(x: int, y: int) -> None:
    used[x][y] = True

    def check(x: int, y: int) -> bool:
        return 0 <= x and x < HEIGHT and 0 <= y and y < WIDTH

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(delta)
    for d in delta:
        _x = x + d[0]
        _y = y + d[1]
        if check(_x, _y) and not used[_x][_y]:
            if d == (-1, 0):
                walls[_x][y][0] = False
            if d == (1, 0):
                walls[x][y][0] = False
            if d == (0, -1):
                walls[x][_y][1] = False
            if d == (0, 1):
                walls[x][y][1] = False
            make_labirint(_x, _y)


make_labirint(0, 0)

# display with Pygame

pygame.init()
size = (1024, 640)
screen = pygame.display.set_mode(size)

status_button = 0
font = pygame.font.SysFont("Arial", 50)
cell = 30

LEFT = 100
UP = 100

INF = 100000

y_start = 0
y_finish = 0
x_start = 0
x_finish = 0


def main() -> None:
    def is_button_down(x: int, y: int, size_of_button: int) -> bool:
        global event
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if x < x1 and x1 < x + size_of_button[0] and y < y1 and y1 < y + size_of_button[1]:
                return False
        return True

    def draw_button(text, x, y, size_of_button, size_text, color_of_button):
        global font, event
        font = pygame.font.SysFont("Arial", size_text)
        pygame.draw.rect(screen, color_of_button, (x - 10, y - 10, size_of_button[0] + 20, size_of_button[1] + 20), 0)
        text = font.render(text, True, (0, 0, 0))
        screen.blit(text, (x, y))

    def write_text_all(text, status_fill, x, y, color_of_text, size_text):
        font = pygame.font.SysFont("Arial", size_text)
        if status_fill:
            screen.fill((255, 255, 255))
        text = font.render(text, True, color_of_text)
        screen.blit(text, (x, y))

    def slide_1_introduction() -> None:
        write_text_all("Привет!", True, 400, 45, (0, 0, 0), 50)
        write_text_all("Эта программа генерирует рандомный лабиринт", False, 75, 125, (0, 0, 0), 40)
        write_text_all("и дает пройти его.", False, 450, 75, (0, 0, 0), 40)
        write_text_all("Нажмите Далее, чтобы продолжить.", False, 150, 275, (0, 0, 0), 40)
        write_text_all("Влад Бурмистров, 2021", False, 400, 550, (0, 0, 0), 30)
        draw_button("Далее", 450, 400, (150, 60), 50, (0, 227, 235))
        pygame.display.update()

    def draw() -> None:
        global cell, y_start, y_finish, x_start, x_finish
        screen.fill((255, 255, 255))
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if walls[i][j][0]:
                    pygame.draw.line(screen, (0, 0, 0), [LEFT + cell * i, UP + cell * j],
                                     [LEFT + cell * (i + 1), UP + cell * j], 1)
                if walls[i][j][1]:
                    pygame.draw.line(screen, (0, 0, 0), [LEFT + cell * i, UP + cell * j],
                                     [LEFT + cell * i, UP + cell * (j + 1)], 1)
                if i == x_start and j == y_start:
                    pygame.draw.rect(screen, (255, 0, 0), (LEFT + i * cell, UP + j * cell, cell, cell), 0)
                if i == x_finish and j == y_finish:
                    pygame.draw.rect(screen, (115, 0, 255), (LEFT + i * cell, UP + j * cell, cell, cell), 0)

    def slide_2_make_labirint() -> None:
        global cell, y_start, y_finish, x_start, x_finish
        draw()
        write_text_all("Выберите страрт и финиш.", False, 150, 450, (0, 0, 0), 40)
        draw_button("Пройти лабиринт", 200, 550, (400, 60), 50, (0, 227, 235))

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x -= LEFT
            y -= UP
            x //= cell
            y //= cell
            if y > WIDTH or x > HEIGHT:
                return
            if event.button == 1:
                x_start = x
                y_start = y
            elif event.button == 3:
                x_finish = x
                y_finish = y

    def slide_3_way() -> None:
        global cell, y_start, y_finish, x_start, x_finish, event
        draw()
        draw_button("Вверх.", 800, 400, (60, 50), 24, (0, 227, 235))
        draw_button("Вниз.", 800, 600, (60, 50), 24, (0, 227, 235))
        draw_button("Влево.", 700, 500, (60, 50), 24, (0, 227, 235))
        draw_button("Вправо.", 900, 500, (60, 50), 24, (0, 227, 235))
        print(y_start, x_start)
        if 0 <= x_start < HEIGHT and 0 <= y_start < WIDTH:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not walls[x_start][y_start][0]:
                    if y_start != 0:
                        y_start -= 1
                if event.key == pygame.K_DOWN and not walls[x_start][y_start][0]:
                    if y_start != WIDTH - 1:
                        y_start += 1
                if event.key == pygame.K_LEFT and not walls[x_start][y_start][1]:
                    if x_start != 0:
                        x_start -= 1
                if event.key == pygame.K_RIGHT and not walls[x_start + 1][y_start][1]:
                    if x_start != HEIGHT - 1:
                        x_start += 1

    global status_button
    if status_button == 0:
        slide_1_introduction(){}
        if not is_button_down(450, 400, (150, 60)):
            status_button = max(status_button, 1)
    elif status_button == 1:
        slide_2_make_labirint()
        if not is_button_down(200, 550, (400, 60)):
            status_button = max(status_button, 2)
    else:
        slide_3_way()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        else:
            main()
    pygame.display.update()
