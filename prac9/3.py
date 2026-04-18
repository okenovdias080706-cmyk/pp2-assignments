import pygame
import datetime
import sys

# Инициализация
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

# Важно: файлы 'mickeyclock.png', 'left_arm.png' и 'right_arm.png' должны быть в папке с кодом
main_mickey = pygame.image.load('mickeyclock.png').convert_alpha()
left_hand = pygame.image.load('left_arm.png').convert_alpha()   # Секундная
right_hand = pygame.image.load('right_arm.png').convert_alpha() # Минутная


def rotate_hand(surface, angle):
    rotated_surface = pygame.transform.rotate(surface, -angle)
    rect = rotated_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    return rotated_surface, rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    sec_angle = seconds * 6
    min_angle = minutes * 6

    # 3. Отрисовка
    screen.fill((255, 255, 255))
    
    # Рисуем циферблат (самого Микки)
    screen.blit(main_mickey, (0, 0))

    # Рисуем минутную руку (правую)
    r_hand, r_rect = rotate_hand(right_hand, min_angle)
    screen.blit(r_hand, r_rect)

    # Рисуем секундную руку (левую)
    l_hand, l_rect = rotate_hand(left_hand, sec_angle)
    screen.blit(l_hand, l_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()