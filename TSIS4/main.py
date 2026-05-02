import pygame, sys, config, game, db
pygame.init()
screen = pygame.display.set_mode((config.W, config.H))
pygame.display.set_caption("Dias's Game")
f1, f2 = pygame.font.SysFont("Arial", 40), pygame.font.SysFont("Arial", 25)
st, name, sc, lv = "MENU", "", 0, 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        if e.type == pygame.KEYDOWN:
            if st == "MENU":
                if e.key == pygame.K_RETURN and name.strip(): st = "PLAY"
                elif e.key == pygame.K_BACKSPACE: name = name[:-1]
                elif e.key == pygame.K_l: st = "TOP"
                elif len(name) < 10 and e.unicode.isprintable(): name += e.unicode
            elif st == "GAMEOVER" and e.key == pygame.K_RETURN: st = "MENU"
            elif st == "TOP" and e.key == pygame.K_ESCAPE: st = "MENU"
    screen.fill((0,0,0))
    if st == "MENU":
        screen.blit(f1.render("SNAKE", 1, (255,255,255)), (250, 50))
        clr = (0,255,0) if (pygame.time.get_ticks()//500)%2 else (255,255,255)
        screen.blit(f1.render(f"Name: {name}_", 1, clr), (180, 150))
        screen.blit(f2.render("ENTER - Start | L - Leaderboard", 1, (100,100,100)), (170, 250))
    elif st == "PLAY":
        sc, lv = game.run_game_loop(screen)
        db.save_game_result(name, sc, lv)
        st = "GAMEOVER"
    elif st == "GAMEOVER":
        screen.blit(f1.render("GAME OVER", 1, (255,0,0)), (200, 100))
        screen.blit(f2.render(f"Score: {sc} | Level: {lv}", 1, (255,255,255)), (210, 160))
        screen.blit(f2.render("Press ENTER for Menu", 1, (255,255,255)), (200, 220))
    elif st == "TOP":
        res = db.get_top_scores()
        screen.blit(f1.render("TOP 5", 1, (255,255,255)), (250, 40))
        for i, (n, s) in enumerate(res): screen.blit(f2.render(f"{i+1}. {n} - {s}", 1, (0,255,0)), (220, 100+i*40))
        screen.blit(f2.render("ESC - Back", 1, (255,255,255)), (250, 350))
    pygame.display.update()