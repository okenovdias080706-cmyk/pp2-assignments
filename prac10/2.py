import pygame

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Smooth Paint - No Gaps")
    clock = pygame.time.Clock()

    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE)

    draw_color = BLACK
    mode = 'pen'
    last_pos = None  # Алдыңғы нүктені сақтау үшін
    radius = 3       # Қаламның жуандығы

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: draw_color = RED
                if event.key == pygame.K_g: draw_color = GREEN
                if event.key == pygame.K_b: draw_color = BLUE
                if event.key == pygame.K_k: draw_color = BLACK
                if event.key == pygame.K_p: mode = 'pen'
                if event.key == pygame.K_e: mode = 'eraser'

            # Тышқан басылғанда алдыңғы позицияны жаңарту
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = event.pos

            # Тышқан жіберілгенде алдыңғы позицияны өшіру
            if event.type == pygame.MOUSEBUTTONUP:
                last_pos = None

        # Үздіксіз сурет салу (Сызық арқылы)
        if pygame.mouse.get_pressed()[0]:
            if mode == 'pen':
                if last_pos:
                    # Алдыңғы нүкте мен қазіргі нүктені қосатын сызық
                    pygame.draw.line(canvas, draw_color, last_pos, mouse_pos, radius * 2)
                    # Сызықтардың қосылған жері тегіс болу үшін шеңбер қосамыз
                    pygame.draw.circle(canvas, draw_color, mouse_pos, radius)
                last_pos = mouse_pos
            
            elif mode == 'eraser':
                if last_pos:
                    pygame.draw.line(canvas, WHITE, last_pos, mouse_pos, 20)
                    pygame.draw.circle(canvas, WHITE, mouse_pos, 10)
                last_pos = mouse_pos

        screen.fill(WHITE)
        screen.blit(canvas, (0, 0))
        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()