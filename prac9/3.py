import pygame
import datetime
import sys

pygame.init()

# Экран
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Full Clock")

clock_fps = pygame.time.Clock()

# Суреттер
clock_img = pygame.image.load("clock_body.png").convert_alpha()
sec_hand = pygame.image.load("left_hand.png").convert_alpha()
min_hand = pygame.image.load("right_hand.png").convert_alpha()

clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))

# Центр
center = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)

# Шрифт
font = pygame.font.SysFont("Arial", 40)

# 🔥 Pivot rotate функциясы
def blit_rotate(surface, image, pivot, offset, angle):
    rotated_image = pygame.transform.rotozoom(image, angle, 1)
    rotated_offset = offset.rotate(-angle)
    rect = rotated_image.get_rect(center=pivot + rotated_offset)
    surface.blit(rotated_image, rect)

# Қол ұзындықтары (саусақ көрсету үшін)
sec_offset = pygame.math.Vector2(0, -250)
min_offset = pygame.math.Vector2(0, -180)

running = True
while running:
    screen.fill((0, 0, 0))

    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ⏱ Уақыт
    now = datetime.datetime.now()

    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + now.second / 60
    hours = now.hour

    # Бұрыштар
    sec_angle = -(seconds / 60) * 360
    min_angle = -(minutes / 60) * 360

    # Фон
    screen.blit(clock_img, (0, 0))

    # Қолдар
    blit_rotate(screen, min_hand, center, min_offset, min_angle)
    blit_rotate(screen, sec_hand, center, sec_offset, sec_angle)

    # 🕒 Цифрлық уақыт
    time_text = f"{hours:02}:{int(minutes):02}:{int(seconds):02}"
    text_surface = font.render(time_text, True, (255, 255, 255))
    screen.blit(text_surface, (WIDTH//2 - 80, HEIGHT - 60))

    pygame.display.flip()
    clock_fps.tick(60)

pygame.quit()
sys.exit()