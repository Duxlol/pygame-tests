import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dux' bomb")
run = True

# Load the player image
player_image = pygame.image.load('./images/smallloafy-circle.png')

# Set the initial position of the player image
player_image_rect = player_image.get_rect()
player_image_rect.topleft = (300, 250)

class keystrokes:
    key_images = {
        'W': {
            'normal': pygame.image.load('./keys/W.png'),
            'pressed': pygame.image.load('./keys/W_DARK.png')
        },
        'A': {
            'normal': pygame.image.load('./keys/A.png'),
            'pressed': pygame.image.load('./keys/A_DARK.png')
        },
        'S': {
            'normal': pygame.image.load('./keys/S.png'),
            'pressed': pygame.image.load('./keys/S_DARK.png')
        },
        'D': {
            'normal': pygame.image.load('./keys/D.png'),
            'pressed': pygame.image.load('./keys/D_DARK.png')
        }
    }

    key_states = {
        'W': 'normal',
        'A': 'normal',
        'S': 'normal',
        'D': 'normal'
    }

    # Set the positions for the key images
    key_positions = {
        'W': (100, 100),
        'A': (200, 100),
        'S': (300, 100),
        'D': (400, 100)
    }

    @staticmethod
    def draw_key(key):
        # Get the current state of the key
        state = keystrokes.key_states[key]

        # Get the image based on the key and state
        image = keystrokes.key_images[key][state]

        # Get the position for the key
        x, y = keystrokes.key_positions[key]

        # Draw the key image on the screen
        screen.blit(image, (x, y))

class Button:
    def __init__(self, text, pos, font, bg="black", hover_bg="gray", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.text = text
        self.bg = bg
        self.hover_bg = hover_bg
        self.feedback = feedback
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self):
        button_rect = pygame.Rect(self.x, self.y, 50, 50)

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

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)

button1 = Button(
    "X",
    (1221, 7),
    font=35,
    bg="red",
    hover_bg="darkred",
    feedback="Closed window!"
)

def keyHandler():
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player_image_rect.move_ip(-1, 0)
    if key[pygame.K_d] == True:
        player_image_rect.move_ip(+1, 0)
    if key[pygame.K_w] == True:
        player_image_rect.move_ip(0, -1)
    if key[pygame.K_s] == True:
        player_image_rect.move_ip(0, +1)

while run:
    screen.fill("white")

    # Draw the player image at the player's position
    screen.blit(player_image, player_image_rect)

    button1.draw()
    keyHandler()

    for key in keystrokes.key_positions:
        keystrokes.draw_key(key)

    if button1.check_collision(player_image_rect):
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keystrokes.key_states['W'] = 'pressed'
            elif event.key == pygame.K_a:
                keystrokes.key_states['A'] = 'pressed'
            elif event.key == pygame.K_s:
                keystrokes.key_states['S'] = 'pressed'
            elif event.key == pygame.K_d:
                keystrokes.key_states['D'] = 'pressed'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keystrokes.key_states['W'] = 'normal'
            elif event.key == pygame.K_a:
                keystrokes.key_states['A'] = 'normal'
            elif event.key == pygame.K_s:
                keystrokes.key_states['S'] = 'normal'
            elif event.key == pygame.K_d:
                keystrokes.key_states['D'] = 'normal'
        button1.click(event)

    pygame.display.update()

pygame.quit()
