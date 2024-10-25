import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
width = 1200
height = 800

# Snake block size (increased to make the snake bigger)
snake_block = 50
snake_speed = 10  # Adjust speed to balance the larger size

# Setup display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hungry Snake Game')

# Clock to control the speed
clock = pygame.time.Clock()

# Fonts for score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load snake head image and scale it to the new snake block size
snake_head_img = pygame.image.load("images/snake_head.png")
snake_head_img = pygame.transform.scale(snake_head_img, (snake_block, snake_block))

# Function to display the player's score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list, direction):
    # Rotate the head image based on the current direction
    if direction == "LEFT":
        head_img = pygame.transform.rotate(snake_head_img, 90)
    elif direction == "RIGHT":
        head_img = pygame.transform.rotate(snake_head_img, -90)
    elif direction == "UP":
        head_img = snake_head_img  # No rotation needed for UP
    elif direction == "DOWN":
        head_img = pygame.transform.rotate(snake_head_img, 180)

    # Draw the head of the snake with the rotated image
    display.blit(head_img, (snake_list[-1][0], snake_list[-1][1]))
    
    # Draw the rest of the snake body as green blocks
    for x in snake_list[:-1]:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Function to display game-over message
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Directional changes
    x_change = 0
    y_change = 0

    # Snake body list and initial length
    snake_list = []
    length_of_snake = 1

    # Initial direction (starting as UP)
    direction = "UP"

    # Food location (aligned with the snake block size)
    food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close:
            display.fill(blue)
            display_message("You Lost! Press C-Play Again or Q-Quit", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handling keyboard events for direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x_change = -snake_block
                    y_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    x_change = snake_block
                    y_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    y_change = -snake_block
                    x_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    y_change = snake_block
                    x_change = 0
                    direction = "DOWN"

        # Check for boundary conditions (snake hitting the wall)
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(black)

        # Draw food
        pygame.draw.rect(display, blue, [food_x, food_y, snake_block, snake_block])

        # Update snake's position and increase the length when it eats food
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list, direction)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake has eaten the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()