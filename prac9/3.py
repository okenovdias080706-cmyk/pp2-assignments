import pygame
import datetime
import sys

pygame.init()

# Экран
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perfect Mickey Clock")

clock_fps = pygame.time.Clock()

# Суреттер
clock_img = pygame.image.load("clock_body.png").convert_alpha()
sec_hand = pygame.image.load("left_hand.png").convert_alpha()
min_hand = pygame.image.load("right_hand.png").convert_alpha()

clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))

# Центр
center = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)

# 🔥 Pivot rotate (ең дұрыс әдіс)
def blit_rotate(surface, image, pivot, offset, angle):
    # бұру
    rotated_image = pygame.transform.rotozoom(image, angle, 1)

    # offset айналдыру
    rotated_offset = offset.rotate(-angle)

    # жаңа позиция
    rect = rotated_image.get_rect(center=pivot + rotated_offset)

    # экранға салу
    surface.blit(rotated_image, rect)


# 🔧 Қол ұзындығы (саусақ дәл көрсету үшін)
sec_offset = pygame.math.Vector2(0, -250)  # секунд ұзын
min_offset = pygame.math.Vector2(0, -180)  # минут қысқа

running = True
while running:
    screen.fill((0, 0, 0))

    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ⏱ Уақыт (smooth)
    now = datetime.datetime.now()

    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + now.second / 60

    # 🔄 Бұрыш
    sec_angle = -(seconds / 60) * 360
    min_angle = -(minutes / 60) * 360

    # 🖼 Фон
    screen.blit(clock_img, (0, 0))

    # 🕒 Қолдар (pivot арқылы)
    blit_rotate(screen, min_hand, center, min_offset, min_angle)
    blit_rotate(screen, sec_hand, center, sec_offset, sec_angle)

    pygame.display.flip()
    clock_fps.tick(60)

pygame.quit()
sys.exit()