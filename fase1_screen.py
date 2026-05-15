#Importo o que é necessário para a função
import pygame
from config import *

# from assets import load_assets

def fase1_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Define os tipos de tiles
    PLATF = 1
    EMPTY = -1

    # Define o mapa com os tipos de tiles

    # tile_size = 40 (CHAT)

    # EMPTY = ar
    # PLAT = plataforma
    # START = início
    # GOAL = porta final

    #Tenho que tranformar em variáveis
    MAP = [
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY, EMPTY, EMPTY],
        [PLATF, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, PLATF, EMPTY, EMPTY, EMPTY, EMPTY, PLATF],
        [EMPTY, EMPTY, PLATF, EMPTY, PLATF, PLATF, PLATF, PLATF, EMPTY, PLATF, PLATF, PLATF],
        [PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF],
        [PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF],
    ]
    #Copiei de exemplos pygame (jump_platform.py)

    #Imagens
    img_dir = path.join(path.dirname(__file__), 'img')
    SUN_IMG = 'sun_img'
    MOON_IMG = 'moon_img'
    background = pygame.image.load('img/fundo_1100x700.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
   
    #Ainda temos que ajustar os nomes nas funções


    # Define estados possíveis do jogador
    STILL = 0
    JUMPING = 1
    FALLING = 2

    # Class que representa os blocos do cenário
    class Tile(pygame.sprite.Sprite):

        # Construtor da classe.
        def __init__(self, tile_img, row, column):
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)

            # Aumenta o tamanho do tile.
            tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

            # Define a imagem do tile.
            self.image = tile_img
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()

            # Posiciona o tile
            self.rect.x = TILE_SIZE * column
            self.rect.y = TILE_SIZE * row


    # Classe para o jogador sol
    class Sun(pygame.sprite.Sprite):

        # Construtor da classe.
        def __init__(self, player_img, row, column, blocks):

            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)

            # Define estado atual
            # Usamos o estado para decidir se o jogador pode ou não pular
            self.state = STILL

            # Ajusta o tamanho da imagem
            sun_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

            # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
            self.image = sun_img
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()

            # Guarda os grupos de sprites para tratar as colisões #########??##########
            self.blocks = blocks

            # Posiciona o personagem #########??########## (Não temos tamanhos fixos para a plataforma)
            # row é o índice da linha embaixo do personagem
            self.rect.x = column * TILE_SIZE
            self.rect.bottom = row * TILE_SIZE

            # Inicializa velocidades
            self.speedx = 0
            self.speedy = 0

            # Define altura no mapa
            # Essa variável sempre conterá a maior altura alcançada pelo jogador
            # antes de começar a cair
            self.highest_y = self.rect.bottom

        # Metodo que atualiza a posição do personagem
        def update(self):
            # Vamos tratar os movimentos de maneira independente.
            # Primeiro tentamos andar no eixo y e depois no x.

            # Tenta andar em y
            # Atualiza a velocidade aplicando a aceleração da gravidade
            self.speedy += GRAVITY
            # Atualiza o estado para caindo
            if self.speedy > 0:
                self.state = FALLING
            # Atualiza a posição y
            self.rect.y += self.speedy

            # Atualiza altura no mapa
            if self.state != FALLING:
                self.highest_y = self.rect.bottom

            # Se colidiu com algum bloco, volta para o ponto antes da colisão
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            # Corrige a posição do personagem para antes da colisão
            for collision in collisions:
                # Estava indo para baixo
                if self.speedy > 0:
                    self.rect.bottom = collision.rect.top
                    # Se colidiu com algo, para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL
                # Estava indo para cima
                elif self.speedy < 0:
                    self.rect.top = collision.rect.bottom
                    # Se colidiu com algo, para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL


            # Tenta andar em x
            self.rect.x += self.speedx
            # Corrige a posição caso tenha passado do tamanho da janela
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH - 1
            # Se colidiu com algum bloco, volta para o ponto antes da colisão
            # O personagem não colide com as plataformas quando está andando na horizontal
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            # Corrige a posição do personagem para antes da colisão
            for collision in collisions:
                # Estava indo para a direita
                if self.speedx > 0:
                    self.rect.right = collision.rect.left
                # Estava indo para a esquerda
                elif self.speedx < 0:
                    self.rect.left = collision.rect.right

        # Método que faz o personagem pular
        def jump(self):
            # Só pode pular se ainda não estiver pulando ou caindo
            if self.state == STILL:
                self.speedy -= JUMP_SIZE
                self.state = JUMPING
    
    # Classe para o jogador lua
    class Moon(pygame.sprite.Sprite):

        # Construtor da classe.
        def __init__(self, player_img, row, column, blocks):

            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)

            # Define estado atual
            # Usamos o estado para decidir se o jogador pode ou não pular
            self.state = STILL

            # Ajusta o tamanho da imagem
            player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

            # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
            self.image = player_img
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()

            # Guarda os grupos de sprites para tratar as colisões
            self.blocks = blocks

            # Posiciona o personagem
            # row é o índice da linha embaixo do personagem
            self.rect.x = column * TILE_SIZE
            self.rect.bottom = row * TILE_SIZE 

            # Inicializa velocidades
            self.speedx = 0
            self.speedy = 0

            # Define altura no mapa
            # Essa variável sempre conterá a maior altura alcançada pelo jogador
            # antes de começar a cair
            self.highest_y = self.rect.bottom

        # Metodo que atualiza a posição do personagem
        def update(self):
            # Vamos tratar os movimentos de maneira independente.
            # Primeiro tentamos andar no eixo y e depois no x.

            # Tenta andar em y
            # Atualiza a velocidade aplicando a aceleração da gravidade
            self.speedy += GRAVITY
            # Atualiza o estado para caindo
            if self.speedy > 0:
                self.state = FALLING
            # Atualiza a posição y
            self.rect.y += self.speedy

            # Atualiza altura no mapa
            if self.state != FALLING:
                self.highest_y = self.rect.bottom

            # Se colidiu com algum bloco, volta para o ponto antes da colisão
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            # Corrige a posição do personagem para antes da colisão
            for collision in collisions:
                # Estava indo para baixo
                if self.speedy > 0:
                    self.rect.bottom = collision.rect.top
                    # Se colidiu com algo, para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL
                # Estava indo para cima
                elif self.speedy < 0:
                    self.rect.top = collision.rect.bottom
                    # Se colidiu com algo, para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL

            
            # Tenta andar em x
            self.rect.x += self.speedx
            # Corrige a posição caso tenha passado do tamanho da janela
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH - 1
            # Se colidiu com algum bloco, volta para o ponto antes da colisão
            # O personagem não colide com as plataformas quando está andando na horizontal
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            # Corrige a posição do personagem para antes da colisão
            for collision in collisions:
                # Estava indo para a direita
                if self.speedx > 0:
                    self.rect.right = collision.rect.left
                # Estava indo para a esquerda
                elif self.speedx < 0:
                    self.rect.left = collision.rect.right

        # Método que faz o personagem pular
        def jump(self):
            # Só pode pular se ainda não estiver pulando ou caindo
            if self.state == STILL:
                self.speedy -= JUMP_SIZE
                self.state = JUMPING


    # Carrega todos os assets de uma vez.
    def load_assets(img_dir):
        assets = {}
        assets[SUN_IMG] = pygame.image.load(path.join(img_dir, 'sol.png')).convert_alpha()
        assets[MOON_IMG] = pygame.image.load(path.join(img_dir, 'lua.png')).convert_alpha()
        #tenho que fazer do sol, da lua e da plat
        assets[PLATF] = pygame.image.load(path.join(img_dir, 'Bloco.png')).convert()
        return assets



    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de plataforma.
    # Sprites de plataforma são aqueles que permitem que o jogador passe quando
    # estiver pulando, mas pare quando estiver caindo.
    platforms = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador, independente
    # de onde ele está vindo

    # Cria Sprite do jogador
    player_sun = Sun(assets[SUN_IMG], 12, 5, platforms) #Sol
    player_moon = Moon(assets[MOON_IMG], 12, 2, platforms) #Lua

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == PLATF:
                    platforms.add(tile)

    # Adiciona o jogador no grupo de sprites por último para ser desenhado por cima das plataformas
    all_sprites.add(player_sun)
    all_sprites.add(player_moon)

    DONE = 0
    PLAYING = 1
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player_sun.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player_sun.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player_sun.jump()
                elif event.key == pygame.K_w:
                    player_moon.jump()
                elif event.key == pygame.K_a:
                    player_moon.speedx -= SPEED_X
                elif event.key == pygame.K_d:
                    player_moon.speedx += SPEED_X
                elif event.key == pygame.K_ESCAPE:
                    state = DONE

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player_sun.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player_sun.speedx -= SPEED_X
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_a:
                    player_moon.speedx += SPEED_X
                elif event.key == pygame.K_d:
                    player_moon.speedx -= SPEED_X

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        window.blit(background, (0, 0))
        all_sprites.draw(window)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        # ----- Gera saídas
        
        # tela_texto = assets['font_media'].render("Tela com o seu jogo", True, WHITE)
        # text_rect = tela_texto.get_rect()
        # text_rect.centerx = WIDTH / 2
        # text_rect.centery = 200
        # window.blit(tela_texto, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
