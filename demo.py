import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Dux' bomb")
run = True
player = pygame.Rect((300,250,50,50))
middle = SCREEN_WIDTH/2 + SCREEN_HEIGHT/2

def keyHandler():
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    if key[pygame.K_d] == True:
        player.move_ip(+1,0)
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    if key[pygame.K_s] == True:
        player.move_ip(0,+1)


while run:
    screen.fill("white")
    pygame.draw.rect(screen, "red", player)
    keyHandler()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()