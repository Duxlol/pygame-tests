import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("WASD Keystrokes")

# Load the images for the keys
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

# Set the initial state for the keys
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

def draw_key(key):
    # Get the current state of the key
    state = key_states[key]

    # Get the image based on the key and state
    image = key_images[key][state]

    # Get the position for the key
    x, y = key_positions[key]

    # Draw the key image on the screen
    screen.blit(image, (x, y))

while True:
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw the key images on the screen
    for key in key_positions:
        draw_key(key)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                key_states['W'] = 'pressed'
            elif event.key == pygame.K_a:
                key_states['A'] = 'pressed'
            elif event.key == pygame.K_s:
                key_states['S'] = 'pressed'
            elif event.key == pygame.K_d:
                key_states['D'] = 'pressed'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_states['W'] = 'normal'
            elif event.key == pygame.K_a:
                key_states['A'] = 'normal'
            elif event.key == pygame.K_s:
                key_states['S'] = 'normal'
            elif event.key == pygame.K_d:
                key_states['D'] = 'normal'
