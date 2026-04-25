import pygame, sys
from pygame.locals import *
import random, time

# 1. Бастапқы баптаулар
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Түстер мен экран өлшемі
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0
COIN_COUNT = 0  # Жиналған тиындар саны

DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer Game")

# Қаріптер
font_small = pygame.font.SysFont("Verdana", 20)

# 2. Қарсылас класы
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 70))
        self.image.fill((255, 0, 0)) # Қызыл машина (Enemy)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, 7)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# 3. Ойыншы класы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 70))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(7, 0)
              if pressed_keys[K_UP]:
                  self.rect.move_ip(7,0)

# 4. ТИЫНДАР класы (Жаңа тапсырма)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 215, 0), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, 2)
        if (self.rect.top > 600):
            self.spawn()

    def spawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Ойын циклі
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((200, 200, 200))
    
    score_txt = font_small.render(f"Score: {SCORE}", True, (0,0,0))
    coin_txt = font_small.render(f"Coins: {COIN_COUNT}", True, (0,0,0))
    DISPLAYSURF.blit(score_txt, (10,10))
    DISPLAYSURF.blit(coin_txt, (SCREEN_WIDTH - 110, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, coins):
        COIN_COUNT += 1
        C1.spawn()

    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(2)
        pygame.quit()
        sys.exit(2)
        
    pygame.display.update()
    FramePerSec.tick(FPS)