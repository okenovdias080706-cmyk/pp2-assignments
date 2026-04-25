import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
CELL_SIZE = 15
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dias's game1")

BLACK = (0, 0, 0)
BLUE = (0, 0, 250)
RED = (200, 0, 0)
GREEN = (0, 180, 0)
WHITE=(250,250,250)

WALL = 10

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20)

direction = (CELL_SIZE, 0)

score = 0
level = 1
speed = 3

snake=[(100,100)]
def generate_food():
    while True:
        x = random.randrange( WALL ,WIDTH - WALL, CELL_SIZE)
        y = random.randrange( WALL,HEIGHT - WALL, CELL_SIZE)
        if (x, y) not in snake:
            return (x, y)


food = generate_food()

running = True

while running:
    screen.fill(GREEN)

    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, WALL))
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - WALL, WIDTH, WALL))
    pygame.draw.rect(screen, BLACK, (0, 0, WALL, HEIGHT))
    pygame.draw.rect(screen, BLACK, (WIDTH - WALL, 0, WALL, HEIGHT))

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

    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    if (
        head_x < WALL or
        head_x >= WIDTH - WALL or
        head_y < WALL or
        head_y >= HEIGHT - WALL
    ):
        print("ВЫ ПРОИГРАЛИ.")
        running = False

    if new_head in snake:
        print("ЗМЕЙКА ХОДИЛА НЕ ТУДА!.")
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1

        if score % 3 == 0:
            level += 1
            speed += 2

        food = generate_food()
    else:
        snake.pop()

    for segment in snake:
        pygame.draw.rect(screen, BLUE, (*segment, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()