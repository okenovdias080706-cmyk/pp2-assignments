import pygame
import random

pygame.init()

# Окно
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Динозавр
dino = pygame.Rect(50, 220, 40, 40)
velocity = 0
gravity = 1
jump = -15
on_ground = True

# Препятствия
obstacles = []
spawn_timer = 0

score = 0
font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    screen.fill(WHITE)

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Прыжок
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and on_ground:
        velocity = jump
        on_ground = False

    # Физика
    velocity += gravity
    dino.y += velocity

    if dino.y >= 220:
        dino.y = 220
        on_ground = True

    # Спавн препятствий
    spawn_timer += 1
    if spawn_timer > 60:
        obstacles.append(pygame.Rect(800, 220, 20, 40))
        spawn_timer = 0

    # Движение препятствий
    for obs in obstacles:
        obs.x -= 6

    # Удаление старых
    obstacles = [obs for obs in obstacles if obs.x > -20]

    # Столкновения
    for obs in obstacles:
        if dino.colliderect(obs):
            running = False

    # Отрисовка
    pygame.draw.rect(screen, BLACK, dino)
    for obs in obstacles:
        pygame.draw.rect(screen, BLACK, obs)

    # Счет
    score += 1
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (650, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()