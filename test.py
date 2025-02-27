import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen in fullscreen mode
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Fullscreen width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Blocks")
gridlocations = [
    {'x': 76, 'y': 87, 'width': 22, 'height': 20, 'value': None},
    {'x': 98, 'y': 87, 'width': 22, 'height': 20, 'value': None},
    {'x': 120, 'y': 87, 'width': 22, 'height': 20, 'value': None},
    {'x': 142, 'y': 87, 'width': 22, 'height': 20, 'value': None},
    {'x': 167, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 189, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 211, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 233, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 258, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 280, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 302, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 324, 'y': 88, 'width': 22, 'height': 20, 'value': None},
    {'x': 76, 'y': 109, 'width': 22, 'height': 20, 'value': None},
    {'x': 98, 'y': 109, 'width': 22, 'height': 20, 'value': None},
    {'x': 120, 'y': 109, 'width': 22, 'height': 20, 'value': None},
    {'x': 142, 'y': 109, 'width': 22, 'height': 20, 'value': None},
    {'x': 167, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 189, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 211, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 233, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 257, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 279, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 301, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 323, 'y': 108, 'width': 22, 'height': 20, 'value': None},
    {'x': 76, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 98, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 120, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 142, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 167, 'y': 132, 'width': 22, 'height': 20, 'value': None},
    {'x': 189, 'y': 132, 'width': 22, 'height': 20, 'value': None},
    {'x': 211, 'y': 132, 'width': 22, 'height': 20, 'value': None},
    {'x': 233, 'y': 132, 'width': 22, 'height': 20, 'value': None},
    {'x': 259, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 281, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 303, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 325, 'y': 131, 'width': 22, 'height': 20, 'value': None},
    {'x': 76, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 98, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 120, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 142, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 167, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 189, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 211, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 233, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 258, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 280, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 302, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 324, 'y': 153, 'width': 22, 'height': 20, 'value': None},
    {'x': 76, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 98, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 120, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 142, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 167, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 189, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 211, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 233, 'y': 175, 'width': 22, 'height': 20, 'value': None},
    {'x': 75, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 97, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 119, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 141, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 166, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 188, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 210, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 232, 'y': 196, 'width': 22, 'height': 20, 'value': None},
    {'x': 75, 'y': 218, 'width': 22, 'height': 20, 'value': None},
    {'x': 97, 'y': 218, 'width': 22, 'height': 20, 'value': None},
    {'x': 119, 'y': 218, 'width': 22, 'height': 20, 'value': None},
    {'x': 141, 'y': 218, 'width': 22, 'height': 20, 'value': None},
    {'x': 166, 'y': 217, 'width': 22, 'height': 20, 'value': None},
    {'x': 188, 'y': 217, 'width': 22, 'height': 20, 'value': None},
    {'x': 210, 'y': 217, 'width': 22, 'height': 20, 'value': None},
    {'x': 232, 'y': 217, 'width': 22, 'height': 20, 'value': None},
    {'x': 75, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 97, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 119, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 141, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 167, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 189, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 211, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 233, 'y': 240, 'width': 22, 'height': 20, 'value': None},
    {'x': 75, 'y': 262, 'width': 22, 'height': 20, 'value': None},
    {'x': 97, 'y': 262, 'width': 22, 'height': 20, 'value': None},
    {'x': 119, 'y': 262, 'width': 22, 'height': 20, 'value': None},
    {'x': 141, 'y': 262, 'width': 22, 'height': 20, 'value': None},
    {'x': 75, 'y': 284, 'width': 22, 'height': 20, 'value': None},
    {'x': 97, 'y': 284, 'width': 22, 'height': 20, 'value': None},
    {'x': 119, 'y': 284, 'width': 22, 'height': 20, 'value': None},
    {'x': 141, 'y': 284, 'width': 22, 'height': 20, 'value': None},
    {'x': 76, 'y': 306, 'width': 22, 'height': 20, 'value': None},
    {'x': 98, 'y': 306, 'width': 22, 'height': 20, 'value': None},
    {'x': 120, 'y': 306, 'width': 22, 'height': 20, 'value': None},
    {'x': 142, 'y': 306, 'width': 22, 'height': 20, 'value': None},
    {'x': 76, 'y': 328, 'width': 22, 'height': 20, 'value': None},
    {'x': 98, 'y': 328, 'width': 22, 'height': 20, 'value': None},
    {'x': 120, 'y': 328, 'width': 22, 'height': 20, 'value': None},
    {'x': 142, 'y': 328, 'width': 22, 'height': 20, 'value': None}
]




background = pygame.image.load("/Users/charlotteeverhart/Downloads/speakeasy.jpg")
grid = pygame.image.load("grid.png")

# Scale the background to cover the entire screen
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

# Resize overlay image to fit as a block (make sure to adjust if needed)
grid = pygame.transform.smoothscale(grid, (350, 350))

# Define colors for the blocks (excluding the overlay block)
colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]  # Red, Blue, Green, Yellow
original_positions = [(0, HEIGHT-100), (0, HEIGHT - 100), (WIDTH - 100, HEIGHT - 100)]  # Top-left, Bottom-left, Bottom-right, Top-right
block_size = 100
blocks = []

# Define clock for controlling frame rate
clock = pygame.time.Clock()

# Create a Block class
class Block:
    def __init__(self, color, original_pos, is_overlay=False, ):
        self.color = color
        self.original_pos = original_pos
        self.x, self.y = original_pos
        self.size = block_size
        self.expanded = False
        self.target_size = block_size
        self.growth_rate = 5  # How fast the block expands (increase for faster)
        self.is_overlay = is_overlay

    def draw(self):
        #if self.is_overlay:
            # screen.blit(self.image_pathway, (self.x, self.y))  # Draw the overlay image instead of a colored block
        #else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def expand(self):
        if not self.expanded:
            self.size = 100
            self.expanded = True
            self.target_size = 400  # New target size for expansion (can change this value)

    def reset(self):
        if self.expanded:
            self.expanded = False
            self.target_size = block_size

    def update_size(self):
        # Gradually increase or decrease the size
        if self.expanded and self.size < self.target_size:
            self.size += self.growth_rate
        elif not self.expanded and self.size > block_size:
            self.size -= self.growth_rate

    def update_position(self):
        if self.expanded:
            self.x = (WIDTH - self.size) // 2
            self.y = (HEIGHT - self.size) // 2
        else:
            self.x, self.y = self.original_pos


# Create the blocks
for i, pos in enumerate(original_positions):
    # The block in the bottom-right corner will have the overlay image
    is_overlay = (i == 2)  # Bottom-right block (index 2 in original_positions)
    blocks.append(Block(colors[i] if not is_overlay else (255, 255, 255), pos, is_overlay,))

# Exit button parameters
exit_button_color = (255, 0, 0)  # Red exit button
exit_button_rect = pygame.Rect(WIDTH - 100, 10, 90, 40)  # Exit button in the top-right corner

def is_inside_box(mouse_x, mouse_y, gridlocations):
    for box in gridlocations:
        if box["x"] <= mouse_x <= box["x"] + box["width"] and box["y"] <= mouse_y <= box["y"] + box["height"]:
            # Toggle between X and O
            if box["value"] is None:
                box["value"] = "X"
            elif box["value"] == "X":
                box["value"] = "O"
            else:
                box["value"] = None
# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with a white background

    # Draw the background image, scaled to the screen size
    screen.blit(background, (0, 0))


    # Draw the exit button (a red rectangle)
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Exit", True, (255, 255, 255))  # White text on the red button
    screen.blit(text, (exit_button_rect.x + 20, exit_button_rect.y + 5))  # Position the text inside the button

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(gridlocations)
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            #for i in range (4):
                #gridlocations.append({"x": mouse_x, "y": mouse_y, "width": 22, "height": 20, "value": None })
                #mouse_x = mouse_x+22
            #print(f"x: {mouse_x}, y: {mouse_y}")
            print(gridlocations)
            is_inside_box(mouse_x, mouse_y, gridlocations)


            # Check if the exit button is clicked
            if exit_button_rect.collidepoint(mouse_x, mouse_y):
                running = False  # Close the game

            # Check if any block is clicked
            for block in blocks:
                # Check if the mouse is inside the block's current position
                if block.x <= mouse_x <= block.x + block.size and block.y <= mouse_y <= block.y + block.size:
                    if block.expanded:
                        block.reset()
                    else:
                        block.expand()

    # Update block sizes and positions
    for block in blocks:
        block.update_size()
        block.update_position()

    # Draw all blocks
    for block in blocks:
        block.draw()
    screen.blit(grid, (0,0))
    font = pygame.font.Font(None, 30)  # Adjust size as needed
    for box in gridlocations:
        if box["value"]:  # If box has an X or O
            text = font.render(box["value"], True, (0, 0, 0))  # Black color
            screen.blit(text, (box["x"] + 5, box["y"] + 3))
    pygame.display.flip()  # Update the screen

    # Set the frame rate (60 FPS)
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
