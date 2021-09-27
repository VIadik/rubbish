import pygame


class Circle:
    def __init__(self, v):
        self.r = 0
        self.pos = (0, 0)
        self.v = v

    def new_position(self, pos: tuple):
        self.pos = pos
        self.r = 0

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), self.pos, self.r)

    def update_size(self):
        self.r += self.v


pygame.init()
SIZE = (1024, 640)
screen = pygame.display.set_mode(SIZE)

screen.fill((0, 0, 255))

running = True
FPS = 60
V = 10

clock = pygame.time.Clock()
circle = Circle(V / FPS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                screen.fill((0, 0, 255))

                circle.new_position(event.pos)

    circle.draw()
    circle.update_size()

    clock.tick(FPS)
    pygame.display.flip()
