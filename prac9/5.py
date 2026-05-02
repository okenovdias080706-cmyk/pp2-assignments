import pygame
import os
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dias's Music")
clock = pygame.time.Clock()
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder)
playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".wav") or f.endswith(".mp3")]
current_track = 0
playing = False
def load_track(index):
    try:
        if playlist:
            pygame.mixer.music.load(playlist[index])
            pygame.mixer.music.play()
    except pygame.error:
        print(f"Қате: {playlist[index]} файлын оқу мүмкін емес.")
if playlist:
    load_track(current_track)
    playing = True
def draw_text():
    screen.fill((30, 30, 30))
    if playlist:
        track_name = os.path.basename(playlist[current_track])
        txt = pygame.font.SysFont("Arial", 24).render(f"Играет: {track_name}", True, (255, 255, 255))
        screen.blit(txt, (50, 100))
        guide = pygame.font.SysFont("Arial", 24).render("P: Play/Pause | S: Stop | N: Next | B: Back", True, (200, 200, 200))
        screen.blit(guide, (50, 200))
    else:
        error_txt = pygame.font.SysFont("Arial", 24).render("Плейлист пуст! 'music' папкасына .mp3 салыңыз.", True, (255, 0, 0))
        screen.blit(error_txt, (50, 150))
    pygame.display.flip()
running = True
while running:
    draw_text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if playlist:
                if event.key == pygame.K_p:
                    if playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing = not playing
                if event.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    playing = False
                if event.key == pygame.K_n:
                    current_track = (current_track + 1) % len(playlist)
                    load_track(current_track)
                    playing = True
                if event.key == pygame.K_b:
                    current_track = (current_track - 1) % len(playlist)
                    load_track(current_track)
                    playing = True
    clock.tick(30)
pygame.quit()