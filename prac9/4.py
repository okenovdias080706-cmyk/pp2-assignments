import pygame
import sys

pygame.init()

# Экран
radius = 25
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dias BOL")

clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2
speed = 10

running = True
while running:
    screen.fill((0, 0, 0))

    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x - radius > 0:
            x -= speed

    if keys[pygame.K_RIGHT]:
        if x + radius < WIDTH:
            x += speed

    if keys[pygame.K_UP]:
        if y - radius > 0:
            y -= speed

    if keys[pygame.K_DOWN]:
        if y + radius < HEIGHT:
            y += speed

    pygame.draw.circle(screen, (255, 250, 250), (x, y), 25)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()