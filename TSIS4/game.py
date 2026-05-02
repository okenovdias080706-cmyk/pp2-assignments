import pygame, random, config

GREEN_LIGHT = (170, 215, 80)
GREEN_DARK = (160, 210, 75)

def get_p(): 
    return [random.randrange(0, config.W, 20), random.randrange(0, config.H, 20)]

def run_game_loop(scr):
    snake, d, sc, lv = [[100,100],[80,100],[60,100]], [20,0], 0, 1
    fd, wl, cl = get_p(), [get_p(), get_p()], pygame.time.Clock()
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return 0, 0
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT and d[0] == 0: d = [-20, 0]
                elif e.key == pygame.K_RIGHT and d[0] == 0: d = [20, 0]
                elif e.key == pygame.K_UP and d[1] == 0: d = [0, -20]
                elif e.key == pygame.K_DOWN and d[1] == 0: d = [0, 20]
        
        h = [snake[0][0] + d[0], snake[0][1] + d[1]]
        if h[0]<0 or h[0]>=config.W or h[1]<0 or h[1]>=config.H or h in snake or h in wl: 
            return sc, lv
            
        snake.insert(0, h)
        
        if h == fd:
            sc += 1
            if sc % 3 == 0: lv += 1
            while True:
                fd = get_p()
                if fd not in snake and fd not in wl: break
            wl = [get_p(), get_p()]
        else: 
            snake.pop()

        for row in range(0, config.H, config.CELL):
            for col in range(0, config.W, config.CELL):
                color = GREEN_LIGHT if (row // config.CELL + col // config.CELL) % 2 == 0 else GREEN_DARK
                pygame.draw.rect(scr, color, (col, row, config.CELL, config.CELL))
        for w in wl: 
            pygame.draw.rect(scr, (100,100,100), (w[0], w[1], 20, 20))
            
        pygame.draw.circle(scr, (255, 0, 0), (fd[0] + 10, fd[1] + 10), 10)
        
        for i, s in enumerate(snake):
            color = (0, 0, 255) if i == 0 else (0, 0, 255)
            pygame.draw.rect(scr, color, (s[0], s[1], 20, 20), border_radius=5)

        pygame.display.update()
        cl.tick(5 + lv * 2)