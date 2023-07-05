import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Quest")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game settings
SEQUENCE_LENGTH = 3  # Length of the memory sequence
SEQUENCE_DELAY = 1000  # Time delay between each sequence item (in milliseconds)

sequence = []
player_sequence = []
game_over = False
show_sequence = True
current_sequence_index = 0
score = 0

# Generate a random sequence
def generate_sequence():
    global sequence
    sequence = []
    for _ in range(SEQUENCE_LENGTH):
        sequence.append(random.choice([RED, GREEN, BLUE]))

# Draw the colored buttons
def draw_buttons():
    button_width = 200
    button_height = 200
    button_margin = 50

    red_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width - button_margin // 2,
                                  SCREEN_HEIGHT // 2 - button_height // 2,
                                  button_width,
                                  button_height)
    pygame.draw.rect(screen, RED, red_button_rect)

    green_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2,
                                    SCREEN_HEIGHT // 2 - button_height // 2,
                                    button_width,
                                    button_height)
    pygame.draw.rect(screen, GREEN, green_button_rect)

    blue_button_rect = pygame.Rect(SCREEN_WIDTH // 2 + button_margin // 2,
                                   SCREEN_HEIGHT // 2 - button_height // 2,
                                   button_width,
                                   button_height)
    pygame.draw.rect(screen, BLUE, blue_button_rect)

# Show the current sequence to the player
def show_sequence_to_player():
    global show_sequence, current_sequence_index
    if current_sequence_index < len(sequence):
        pygame.time.set_timer(pygame.USEREVENT, SEQUENCE_DELAY)
        draw_buttons()
        current_color = sequence[current_sequence_index]
        flash_button(current_color)
        current_sequence_index += 1
    else:
        show_sequence = False
        current_sequence_index = 0

# Flash a button with a specific color
def flash_button(color):
    button_rect = pygame.Rect(0, 0, 200, 200)
    if color == RED:
        button_rect.center = (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2)
    elif color == GREEN:
        button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    elif color == BLUE:
        button_rect.center = (SCREEN_WIDTH // 2 + 250, SCREEN_HEIGHT // 2)

    pygame.draw.rect(screen, color, button_rect)
    pygame.display.flip()
    pygame.time.wait(300)
    pygame.draw.rect(screen, BLACK, button_rect)
    pygame.display.flip()
    pygame.time.wait(300)

# Check if the player sequence matches the original sequence
def check_sequence():
    global game_over, player_sequence, score
    if player_sequence != sequence:
        game_over = True
    else:
        score += 1
        player_sequence = []

# Display game over screen
def game_over_screen():
    screen.fill(BLACK)

    text_surface = font.render("Game Over", True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text_surface, text_rect)

    score_surface = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(score_surface, score_rect)

    pygame.display.flip()
    pygame.time.wait(2000)

# Main game loop
def game_loop():
    global player_sequence, game_over, show_sequence, current_sequence_index, score

    generate_sequence()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and not show_sequence:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    if SCREEN_WIDTH // 2 - 250 <= x <= SCREEN_WIDTH // 2 - 50 and \
                            SCREEN_HEIGHT // 2 - 100 <= y <= SCREEN_HEIGHT // 2 + 100:
                        player_sequence.append(RED)
                    elif SCREEN_WIDTH // 2 - 100 <= x <= SCREEN_WIDTH // 2 + 100 and \
                            SCREEN_HEIGHT // 2 - 100 <= y <= SCREEN_HEIGHT // 2 + 100:
                        player_sequence.append(GREEN)
                    elif SCREEN_WIDTH // 2 + 50 <= x <= SCREEN_WIDTH // 2 + 250 and \
                            SCREEN_HEIGHT // 2 - 100 <= y <= SCREEN_HEIGHT // 2 + 100:
                        player_sequence.append(BLUE)
            elif event.type == pygame.USEREVENT and show_sequence:
                show_sequence_to_player()

        screen.fill(BLACK)

        if show_sequence:
            show_sequence_to_player()
        else:
            draw_buttons()
            check_sequence()

        pygame.display.flip()
        clock.tick(60)

    game_over_screen()
    game_loop()

# Start the game loop
game_loop()

pygame.quit()
