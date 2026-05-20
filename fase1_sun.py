#Importo o que é necessário para a função
import pygame
from config import *
import random

# from assets import load_assets

def fase1_sun_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Define os tipos de tiles
    PLATF = 1
    EMPTY = -1

    # Define o mapa com os tipos de tiles

    # tile_size = 40 (CHAT)
    img_dir = path.join(path.dirname(__file__), 'img')
    assets = {}
    assets["score_font"] = pygame.font.Font(path.join(img_dir, 'PressStart2P.ttf'), 28)
        
    # EMPTY = ar
    # PLAT = plataforma
    # START = início
    # GOAL = porta final
    state = F1SUN
    #Tenho que tranformar em variáveis]
    clock = pygame.time.Clock()
    i = 0
    while state == F1SUN:
        i+= 1
        clock.tick(FPS)
        window.fill((0,0,0))
        text_surface = assets['score_font'].render("Sol ganhou", True, (200,200,200))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
        pygame.display.update()

        if i > FPS * 3:
            return F1