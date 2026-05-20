# ===== Inicialização =====

#Importo e inicio pacotes
import pygame
import random
from fase1_screen import fase1_screen
from fase1_sun import fase1_sun_screen
# from fase2_screen import fase2_screen
# from fase3_screen import fase3_screen

#Parâmetros necessários (também importei)
from config import *

#Para organizar a lógica, é aqui que acontece tudo dos outros arquivos

#Início do jogo
pygame.init()
pygame.mixer.init()

#Gerando tela principal + título
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption('Corrida espacial')

#Loop das fases
state = F1
while state != QUIT:
    print("State: ", state)
    # if state == INIT:
    #     state = init_screen(window)
    if state == F1:
        state = fase1_screen(window)
    elif state == F1SUN:
        state = fase1_sun_screen(window)
    elif state == F2:
        # state = fase2_screen(window)
        pass
    elif state == F3:
        # state = fase3_screen(window)
        pass
    else:
        state = QUIT

#Finalização (Ver se precisa fazer aquilo de clicar no exit para quit)
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
