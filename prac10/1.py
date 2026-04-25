import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
CELL_SIZE = 15
screen = pygame.display.set_mode((WIDTH, HEIGHT))
colums=screen // CELL_SIZE
rows=screen //CELL_SIZE
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

BORDER_THICKNESS = 10

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20)

snake = [(100, 100)]
direction = (CELL_SIZE, 0)

score = 0
level = 1
speed = 7

def generate_food():
    while True:
        x = random.randrange(BORDER_THICKNESS, WIDTH - BORDER_THICKNESS, CELL_SIZE)
        y = random.randrange(BORDER_THICKNESS, HEIGHT - BORDER_THICKNESS, CELL_SIZE)
        if (x, y) not in snake:
            return (x, y)


food = generate_food()

running = True

while running:
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, BORDER_THICKNESS))  # top
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - BORDER_THICKNESS, WIDTH, BORDER_THICKNESS))  # bottom
    pygame.draw.rect(screen, WHITE, (0, 0, BORDER_THICKNESS, HEIGHT))  # left
    pygame.draw.rect(screen, WHITE, (WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, HEIGHT))  # right

    # --- EVENTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN:
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT:
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (CELL_SIZE, 0)

    # --- MOVE SNAKE ---
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # --- WALL COLLISION ---
    if (
        head_x < BORDER_THICKNESS or
        head_x >= WIDTH - BORDER_THICKNESS or
        head_y < BORDER_THICKNESS or
        head_y >= HEIGHT - BORDER_THICKNESS
    ):
        print("Game Over! Hit the wall.")
        running = False

    # --- SELF COLLISION ---
    if new_head in snake:
        print("Game Over! Hit yourself.")
        running = False

    snake.insert(0, new_head)

    # --- FOOD ---
    if new_head == food:
        score += 1

        # LEVEL UP every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2

        food = generate_food()
    else:
        snake.pop()

    # --- DRAW SNAKE ---
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # --- DRAW FOOD ---
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # --- UI ---
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    # Speed control
    clock.tick(speed)

pygame.quit()