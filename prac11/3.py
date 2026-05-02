import pygame

# 1. Инициализация
pygame.init()

# Экран өлшемдері
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINT")

# Түстер
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Бастапқы күй
draw_color = BLACK
brush_size = 5
painting = False
start_pos = None  # Фигураның басталған нүктесі
last_pos = None   # Еркін салу үшін
mode = 'brush'    # Режимдер: 'brush', 'rect', 'circle', 'line'

screen.fill(WHITE)
# Экранның таза көшірмесін сақтау (фигураны салғанда керек)
canvas = screen.copy()

def draw_menu():
    """Басқару панелін салу"""
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 70))
    
    # Түстерді таңдау шаршылары
    colors = [BLACK, RED, GREEN, BLUE, WHITE, YELLOW]
    for i, col in enumerate(colors):
        pygame.draw.rect(screen, col, (10 + i*40, 10, 30, 30))
        if col == WHITE:
            pygame.draw.rect(screen, BLACK, (10 + i*40, 10, 30, 30), 1)

    # Режимдерді таңдау мәтіні
    font = pygame.font.SysFont("Arial", 16)
    controls = "Brush: [ 1 ] | Rect: [ 2 ] | Circle: [ 3 ] | Line: [ 4 ]"
    actions = "Size: [ + / - ] | Clear: [ SPACE ]"
    
    screen.blit(font.render(controls, True, BLACK), (270, 10))
    screen.blit(font.render(actions, True, BLACK), (270, 40))
    screen.blit(font.render(f"Mode: {mode.upper()}", True, BLUE), (650, 25))

# Ойын циклы
run = True
while run:
    draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > 70:
                painting = True
                start_pos = event.pos
                last_pos = event.pos
                # Фигура салмас бұрын экранды жаттап алу
                canvas.blit(screen, (0, 0))
            else:
                x = event.pos[0]
                if 10 <= x <= 40: draw_color = BLACK
                elif 50 <= x <= 80: draw_color = RED
                elif 90 <= x <= 120: draw_color = GREEN
                elif 130 <= x <= 160: draw_color = BLUE
                elif 170 <= x <= 200: draw_color = WHITE
                elif 210 <= x <= 240: draw_color = YELLOW

        if event.type == pygame.MOUSEBUTTONUP:
            painting = False
            last_pos = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x: mode = 'brush'
            if event.key == pygame.K_z: mode = 'rect'
            if event.key == pygame.K_c: mode = 'circle'
            if event.key == pygame.K_v: mode = 'line'
            if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS: brush_size += 1
            if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                if brush_size > 1: brush_size -= 1
            if event.key == pygame.K_SPACE:
                screen.fill(WHITE)
                canvas.fill(WHITE)

    if painting:
        current_pos = pygame.mouse.get_pos()
        if current_pos[1] > 70:
            if mode == 'brush':
                pygame.draw.line(screen, draw_color, last_pos, current_pos, brush_size * 2)
                pygame.draw.circle(screen, draw_color, current_pos, brush_size)
                last_pos = current_pos
            
            elif mode == 'rect':
                screen.blit(canvas, (0, 0)) # Ескі экранды қалпына келтіру
                width = current_pos[0] - start_pos[0]
                height = current_pos[1] - start_pos[1]
                pygame.draw.rect(screen, draw_color, (start_pos[0], start_pos[1], width, height), brush_size)
            
            elif mode == 'circle':
                screen.blit(canvas, (0, 0))
                radius = int(((current_pos[0] - start_pos[0])**2 + (current_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, draw_color, start_pos, radius, brush_size)
            
            elif mode == 'line':
                screen.blit(canvas, (0, 0))
                pygame.draw.line(screen, draw_color, start_pos, current_pos, brush_size * 2)

    pygame.display.update()

pygame.quit()