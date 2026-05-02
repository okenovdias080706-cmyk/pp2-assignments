import pygame
import random
import time

pygame.init()

LIGHT_GREEN = (170, 215, 80)
DARK_GREEN = (160, 210, 75)
SNAKE_COLOR = (70, 110, 240)
FOOD_COLOR = (235, 70, 30)
TEXT_COLOR = (255, 255, 255)
UI_GREEN = (90, 140, 50)

WIDTH, HEIGHT = 600, 600
BOX = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25, bold=True)

def draw_grid():
    for row in range(HEIGHT // BOX):
        for col in range(WIDTH // BOX):
            color = LIGHT_GREEN if (row + col) % 2 == 0 else DARK_GREEN
            pygame.draw.rect(screen, color, (col * BOX, row * BOX, BOX, BOX))

def show_score(score):
    value = font.render(f"ОЧКО: {score}", True, TEXT_COLOR)
    screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake_list = [[x, y]]
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - BOX) / BOX) * BOX
    foody = round(random.randrange(0, HEIGHT - BOX) / BOX) * BOX
    if foodx == x and foody == y:
        if (x,y) in snake_list:
            foodx = round(random.randrange(0, WIDTH - BOX) / BOX) * BOX
            foody = round(random.randrange(0, HEIGHT - BOX) / BOX) * BOX 

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BOX, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BOX, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BOX
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BOX

        # Қабырғаға соғылуды тексеру
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        x += dx
        y += dy
        
        draw_grid()
        
        # Алманы салу
        pygame.draw.circle(screen, FOOD_COLOR, (foodx + BOX//2, foody + BOX//2), BOX//2 - 2)

        # Жыланның басын қосу
        snake_head = [x, y]
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Өз денесіне соғылуды тексеру
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Жыланды салу
        for i, segment in enumerate(snake_list):
            # Басы сәл өзгеше түс болуы мүмкін
            color = (60, 100, 220) if i == len(snake_list) - 1 else SNAKE_COLOR
            pygame.draw.rect(screen, color, [segment[0], segment[1], BOX, BOX], border_radius=8)

        # Алманы жегенді тексеру
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, WIDTH - BOX) / BOX) * BOX
            foody = round(random.randrange(0, HEIGHT - BOX) / BOX) * BOX
            length_of_snake += 1

        show_score(length_of_snake - 1)
        pygame.display.update()

        # Ойын жылдамдығы
        clock.tick(7)

    pygame.quit()
    quit()

game_loop()