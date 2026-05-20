from os import path

#MUDAR
# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')
#temos que fazer ainda. Não entendi

# Dados gerais do jogo.
WIDTH = 1100 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo
PLAYER_WIDTH=50
PLAYER_HEIGHT=50
GRAVITY=5
TILE_SIZE = 50 # Tamanho de cada tile (cada tile é um quadrado)
METEOR_WIDTH = 50
METEOR_HEIGHT = 50
STAR_WIDTH = 30
STAR_HEIGHT = 30
DOOR_WIDTH=60
DOOR_HEIGHT=60
JUMP_SIZE= TILE_SIZE
SPEED_X=5

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
F1= 3
F1SUN = 6
F2= 4
F3= 5
