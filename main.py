import pygame

WIDTH = 1280
HEIGHT = 720
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fps = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = pygame.image.load("images/smallloafy-circle.png")

class Player(object):
    def __init__(self):
        self.image = pygame.image.load("images/smallloafy-circle.png")
        self.flipped = False
        self.x = 0
        self.y = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
            self.flipped = False
        elif key[pygame.K_LEFT]:
            self.x -= dist
            self.flipped = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

pygame.quit()