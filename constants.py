import pygame

WIDTH=800
HEIGHT=600
RED=(255,0,0)

screen=pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND=pygame.image.load("./img/BG.png")
BACKGROUND=pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT)).convert_alpha()
BACKGROUND_PLATFORM=pygame.image.load("./img/fruit ninja/platform.png")
BACKGROUND_PLATFORM=pygame.transform.scale(BACKGROUND_PLATFORM, (WIDTH/3*2, HEIGHT/2)).convert_alpha()
BACKGROUND_PLATFORM_RECT=BACKGROUND_PLATFORM.get_rect(topleft=(WIDTH/6, HEIGHT/3*2))
