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

# Get original background dimensions
bg_width, bg_height = background.get_size()

# Calculate the best scale factor to fill the entire screen
scale_factor = max(WIDTH / bg_width, HEIGHT / bg_height)

# New scaled width and height for background
new_width = int(bg_width * scale_factor)
new_height = int(bg_height * scale_factor)

# Resize background while keeping proportions
background = pygame.transform.smoothscale(background, (new_width, new_height))

# Calculate position to crop (center the image)
x_offset = (new_width - WIDTH) // 2
y_offset = (new_height - HEIGHT) // 2

# Resize overlay image
overlay = pygame.transform.smoothscale(overlay, (400, 400))  # Resize overlay image

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
start_button_text = font.render("PLAY", True, (255, 255, 255))  # Start button text

# Game loop flag
# game_started = False
game_started = True

# Start screen loop
while not game_started:
    screen.fill((0, 0, 0))  # Fill the screen with black (start screen background)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            # Check if Start button is clicked
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                game_started = True  # Start the game

    # Check if mouse is over the exit button
    if button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, button_hover_color, button_rect)  # Highlight button
    else:
        pygame.draw.rect(screen, button_color, button_rect)  # Normal button

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            if button_rect.collidepoint(mouse_x, mouse_y):  # Check if clicked
                running = False  # Exit the game

    # Draw Start screen title
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("A Murder in the Speakeasy", True, (255, 255, 255))
    # screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
    # Draw button text
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 10))

    # Draw Start button
    if start_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, button_hover_color, start_button_rect)  # Hover color
    else:
        pygame.draw.rect(screen, button_color, start_button_rect)  # Normal button color

    # Draw "START" text on the button
    screen.blit(start_button_text, (start_button_rect.x + 60, start_button_rect.y + 10))

    # Update the display
    pygame.display.flip()

running = True
while running:
    keys = pygame.key.get_pressed()

    # Draw background (centered)
    screen.blit(background, (-x_offset, -y_offset))

    # Draw overlay image in bottom-right
    screen.blit(overlay, (overlay_x, overlay_y))

    # Update the display
    pygame.display.flip()


class OverlaySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)  # Load the image
        self.image = pygame.transform.scale(self.image, (500, 500))  # Scale the sprite
        self.rect = self.image.get_rect()  # Get the rectangle for positioning
        self.rect.topleft = (x, y)  # Set initial position
        self.y_velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.on_ground = False

    def update(self, keys, background_width, background_height):
        # Move left and right
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2

        # Jumping logic
        if self.on_ground and keys[pygame.K_SPACE]:
            self.y_velocity = self.jump_strength
            self.on_ground = False

        self.y_velocity += self.gravity  # Apply gravity
        self.rect.y += self.y_velocity

        # Boundary checking
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > background_width:
            self.rect.right = background_width

        # Ground collision
        if self.rect.bottom >= background_height:
            self.rect.bottom = background_height
            self.y_velocity = 0
            self.on_ground = True


# Create sprite
overlay = OverlaySprite("/Users/charlotteeverhart/Downloads/IMG_3847.PNG", 0, 0)
overlay2 = OverlaySprite("/Users/charlotteeverhart/Desktop/dead_amongus.PNG", 0, 0)
all_sprites = pygame.sprite.Group(overlay, overlay2)

all_sprites.update(keys, WIDTH, HEIGHT)
all_sprites.draw(screen)

'''
running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Redraw the screen
    screen.blit(background, (0, 0))
    #
    pygame.display.flip()
'''

pygame.quit()