import pygame

# Initialize Pygame
pygame.init()

# Get full screen size
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h  # Match screen size

# Set up fullscreen display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Speakeasy")

# Load images
background = pygame.image.load("/Users/charlotteeverhart/Downloads/speakeasy.jpg")
overlay = pygame.image.load("grid.png")
victim = pygame.image.load("victimbodypic.jpg")

# Get original background dimensions
bg_width, bg_height = background.get_size()

# Calculate the best scale factor to fill the entire screen
scale_factor = max(WIDTH / bg_width, HEIGHT / bg_height)

# New scaled width and height for background
new_width = int(bg_width * scale_factor)
new_height = int(bg_height * scale_factor)

# Resize background while keeping proportions
background = pygame.transform.smoothscale(background, (new_width, new_height))

startScreen = pygame.transform.smoothscale(victim, (new_width,new_height))

# Calculate position to crop (center the image)
x_offset = (new_width - WIDTH) // 2
y_offset = (new_height - HEIGHT) // 2

# Resize overlay image
overlay = pygame.transform.scale(overlay, (500, 500))  # Resize overlay image

# Position overlay in bottom-right corner
overlay_x = WIDTH - overlay.get_width()
overlay_y = HEIGHT - overlay.get_height()

# Define exit button properties
button_color = (200, 0, 0)  # Red button
button_hover_color = (255, 50, 50)  # Lighter red on hover
button_rect = pygame.Rect(WIDTH - 120, 20, 100, 50)  # Position top-right
font = pygame.font.Font(None, 36)  # Button text font
button_text = font.render("EXIT", True, (255, 255, 255))  # White text

# Define Start screen button properties
start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)  # Centered button
start_button_text = font.render("START", True, (255, 255, 255))  # Start button text

# Game loop flag
game_started = False

# Start screen loop
while not game_started:
    screen.blit(startScreen, (-x_offset, -y_offset))  # Fill the screen with black (start screen background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            # Check if Start button is clicked
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                game_started = True  # Start the game

    # Draw Start screen title
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Welcome to Speakeasy", True, (0, 0, 0))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

    # Draw Start button
    if start_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, button_hover_color, start_button_rect)  # Hover color
    else:
        pygame.draw.rect(screen, button_color, start_button_rect)  # Normal button color

    # Draw "START" text on the button
    screen.blit(start_button_text, (start_button_rect.x + 60, start_button_rect.y + 10))

    # Update the display
    pygame.display.flip()

# Main game loop (after Start button is clicked)
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            if button_rect.collidepoint(mouse_x, mouse_y):  # Check if clicked
                running = False  # Exit the game

    # Draw background (centered)
    screen.blit(background, (-x_offset, -y_offset))

    # Draw overlay image in bottom-right
    screen.blit(overlay, (overlay_x, overlay_y))

    # Check if mouse is over the exit button
    if button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, button_hover_color, button_rect)  # Highlight button
    else:
        pygame.draw.rect(screen, button_color, button_rect)  # Normal button

    # Draw button text
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 10))

    # Update the display
    pygame.display.flip()

pygame.quit()