import pygame
import random

# Инициализация
pygame.init()

# Экран өлшемі
WIDTH, HEIGHT = 400, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Түстер
WHITE = (255, 255, 255)

# --- СУРЕТТЕРДІ ЖҮКТЕУ ---
# Ескерту: Файлдар кодпен бір папкада болуы керек
try:
    player_img = pygame.image.load('car.png')
    enemy_img = pygame.image.load('enemy_car.png')
    road_img = pygame.image.load('road.png')
    # Суреттерді экранға сәйкестендіру (өлшемін өзгерту)
    player_img = pygame.transform.scale(player_img, (50, 90))
    enemy_img = pygame.transform.scale(enemy_img, (50, 90))
    road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
except:
    print("Суреттер табылмады! Стандартты тіктөртбұрыштар қолданылады.")
    player_img = None

# Ойын параметрлері
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28, bold=True)

def show_score(score):
    score_txt = font.render(f"Ұпай: {score}", True, WHITE)
    screen.blit(score_txt, (10, 10))

def game_loop():
    # Ойыншының бастапқы орны
    x = WIDTH // 2 - 25
    y = HEIGHT - 120
    x_change = 0
    
    # Кедергілер
    enemy_x = random.randrange(50, WIDTH - 100)
    enemy_y = -100
    enemy_speed = 7
    
    # Жолдың қозғалысы үшін
    road_y = 0
    score = 0
    
    run = True
    while run:
        # 1. Оқиғаларды өңдеу
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                if event.key == pygame.K_RIGHT:
                    x_change = 8
            if event.type == pygame.KEYUP:
                x_change = 0

        # 2. Логика (Қозғалыс)
        x += x_change
        enemy_y += enemy_speed
        
        # Жолдың төмен жылжуы (шексіз эффект)
        road_y += enemy_speed
        if road_y >= HEIGHT:
            road_y = 0

        # 3. Суреттерді экранға шығару
        # Жолды екі рет саламыз (бірінің астына бірін), шексіздік үшін
        if road_img:
            screen.blit(road_img, (0, road_y))
            screen.blit(road_img, (0, road_y - HEIGHT))
        else:
            screen.fill((50, 50, 50))

        # Кедергі машина
        if enemy_img:
            screen.blit(enemy_img, (enemy_x, enemy_y))
        
        # Ойыншы машинасы
        if player_img:
            screen.blit(player_img, (x, y))

        # 4. Ұпай жинау және кедергіні жаңарту
        if enemy_y > HEIGHT:
            enemy_y = -100
            enemy_x = random.randrange(50, WIDTH - 100)
            score += 1
            enemy_speed += 0.2 # Ойын бірте-бірте қиындайды

        # 5. Соқтығысуды тексеру
        # Ойыншы шекарадан шықса
        if x < 40 or x > WIDTH - 90:
            run = False
        
        # Машиналар соғылса (Rect collision)
        player_rect = pygame.Rect(x, y, 50, 90)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 90)
        if player_rect.colliderect(enemy_rect):
            run = False

        show_score(score)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_loop()