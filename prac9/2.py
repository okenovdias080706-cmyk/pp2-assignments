import pygame  # pygame кітапханасын қосу

pygame.init()  # Барлық модульдерді іске қосу

# 1. Терезе параметрлері
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("My First Game")

running = True 
while running: 
    # 2. Оқиғаларды тексеру (мысалы, терезені жабу)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    # 3. Экрады фонмен толтыру (алдыңғы кадрды өшіру үшін)
    screen.fill((250, 0, 0)) # Қара түс

    # 4. Геометриялық фигураларды салу (БҰЛ ЖЕРДЕ СЫЗЫЛАДЫ)
    # Қызыл төртбұрыш (x, y, ені, биіктігі)
    pygame.draw.rect(screen, (100, 150, 200), (400, 300, 150, 150)) 

    # Көк шеңбер (центр_x, center_y, радиусы)
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 50)

    # Жасыл сызық (басы, соңы, қалыңдығы)
    pygame.draw.line(screen, (0, 255, 0), (0, 0), (400, 300), 5)

    # 5. Экранды жаңарту (осысыз ештеңе көрінбейді)
    pygame.display.flip()

pygame.quit() # Программаны тоқтату