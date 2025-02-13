import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Speakeasy")

# Load and scale background
background = pygame.image.load("/Users/charlotteeverhart/Downloads/speakeasy.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Define sprite class
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
overlay2=OverlaySprite("/Users/charlotteeverhart/Desktop/grid.png", 0, 0)
all_sprites = pygame.sprite.Group(overlay, overlay2)

running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update(keys, WIDTH, HEIGHT)

    # Redraw the screen
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()