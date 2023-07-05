import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dux' bomb")
run = True
player = pygame.Rect((300, 250, 50, 50))
middle = SCREEN_WIDTH / 2 + SCREEN_HEIGHT / 2


class Button:
    def __init__(self, text, pos, font, bg="black", hover_bg="gray", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.text = text
        self.bg = bg
        self.hover_bg = hover_bg
        self.feedback = feedback

    def draw(self):
        button_rect = pygame.Rect(self.x, self.y, 200, 50)

        # Check if the mouse hovers over the button
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            bg_color = self.hover_bg
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bg_color = self.bg
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.draw.rect(screen, bg_color, button_rect)
        text_surface = self.font.render(self.text, True, pygame.Color("white"))
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if self.x <= x <= self.x + 200 and self.y <= y <= self.y + 50:
                    pygame.quit()


button1 = Button(
    "Click here",
    (100, 100),
    font=30,
    bg="navy",
    hover_bg="dodgerblue",
    feedback="You clicked me"
)


def keyHandler():
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    if key[pygame.K_d] == True:
        player.move_ip(+1, 0)
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    if key[pygame.K_s] == True:
        player.move_ip(0, +1)


while run:
    screen.fill("white")
    pygame.draw.rect(screen, "red", player)
    button1.draw()  # Draw the button
    keyHandler()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        button1.click(event)  # Handle button click events
    pygame.display.update()

pygame.quit()
