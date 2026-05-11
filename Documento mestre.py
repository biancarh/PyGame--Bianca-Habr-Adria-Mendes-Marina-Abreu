# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, F1, F2, F3, QUIT
from fase1_screen import fase1_screen
# from fase2_screen import fase2_screen
# from fase3_screen import fase3_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Corrida espacial')


state = F1
while state != QUIT:
    # if state == INIT:
    #     state = init_screen(window)
    if state == F1:
        state = fase1_screen(window)
    elif state == F2:
        state = fase2_screen(window)
    elif state == F3:
        state = fase3_screen(window)
    else:
        state = QUIT
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
