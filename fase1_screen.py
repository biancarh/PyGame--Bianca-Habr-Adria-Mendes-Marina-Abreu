#Importo o que é necessário para a função
import pygame
from config import *
import random

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
        
        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,PLATF,PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],

        # plataforma inicial para dois jogadores
        [PLATF,PLATF,PLATF,EMPTY,EMPTY,EMPTY,EMPTY,
        EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,
        EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,
        PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF,PLATF]

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

            self.init_column = column
            self.init_row = row

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

        def reset_position_sun(self):
            self.rect.x = self.init_column * TILE_SIZE
            self.rect.bottom = self.init_row * TILE_SIZE 

            # Inicializa velocidades
            # self.speedx = 0
            # self.speedy = 0

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
            self.init_column = column
            self.init_row = row

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
        
        def reset_position_moon(self):
            self.rect.x = self.init_column * TILE_SIZE
            self.rect.bottom = self.init_row * TILE_SIZE 

            # # Inicializa velocidades
            # self.speedx = 0
            # self.speedy = 0

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

    class Meteor(pygame.sprite.Sprite):
        def __init__(self, assets):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = assets['meteor_img']
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
                self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
                self.rect.y = random.randint(-100, -METEOR_HEIGHT)
                self.speedx = random.randint(-3, 3)
                self.speedy = random.randint(2, 9)  
    
    # Classe que representa uma explosão de meteoro
    class Explosion(pygame.sprite.Sprite):
        # Construtor da classe.
        def __init__(self, center, assets):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            # Armazena a animação de explosão
            self.explosion_anim = assets['explosion_anim']

            # Inicia o processo de animação colocando a primeira imagem na tela.
            self.frame = 0  # Armazena o índice atual na animação
            self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
            self.rect = self.image.get_rect()
            self.rect.center = center  # Posiciona o centro da imagem

            # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
            self.last_update = pygame.time.get_ticks()

            # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
            # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
            # próxima imagem da animação será mostrada
            self.frame_ticks = 50

        def update(self):
            # Verifica o tick atual.
            now = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde a ultima mudança de frame.
            elapsed_ticks = now - self.last_update

            # Se já está na hora de mudar de imagem...
            if elapsed_ticks > self.frame_ticks:
                # Marca o tick da nova imagem.
                self.last_update = now

                # Avança um quadro.
                self.frame += 1

                # Verifica se já chegou no final da animação.
                if self.frame == len(self.explosion_anim):
                    # Se sim, tchau explosão!
                    self.kill()
                else:
                    # Se ainda não chegou ao fim da explosão, troca de imagem.
                    center = self.rect.center
                    self.image = self.explosion_anim[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    
    #Cria a classe da estrela
    class Star(pygame.sprite.Sprite):
        def __init__(self, star_img, row, column):
            pygame.sprite.Sprite.__init__(self)

            self.image = star_img
            self.rect = self.image.get_rect()

            # fica em cima da plataforma
            self.rect.midbottom = (column * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE)

        

    # Carrega todos os assets de uma vez.
    def load_assets(img_dir):
        assets = {}
        assets[SUN_IMG] = pygame.image.load(path.join(img_dir, 'sol.png')).convert_alpha()
        assets[MOON_IMG] = pygame.image.load(path.join(img_dir, 'lua.png')).convert_alpha()
        #tenho que fazer do sol, da lua e da plat
        assets[PLATF] = pygame.image.load(path.join(img_dir, 'Bloco.png')).convert()
        assets['meteor_img'] = pygame.image.load(path.join(img_dir, "meteor_img.png")).convert_alpha()
        assets['meteor_img'] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))
        explosion_anim = []
        for i in range(9):
            # Os arquivos de animação são numerados de 00 a 08
            filename = (path.join(img_dir, 'regularExplosion0{}.png'.format(i)))
            img = pygame.image.load(filename).convert()
            img = pygame.transform.scale(img, (32, 32))
            explosion_anim.append(img)
        assets["explosion_anim"] = explosion_anim
        assets["score_font"] = pygame.font.Font(path.join(img_dir, 'PressStart2P.ttf'), 28)
        assets['star_img'] = pygame.image.load(path.join(img_dir, 'star_img.png')).convert_alpha()
        assets['star_img'] = pygame.transform.scale(assets['star_img'], (STAR_WIDTH, STAR_HEIGHT))
        return assets



    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    all_meteors = pygame.sprite.Group()
    all_stars = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_meteors'] = all_meteors
    groups['all_stars'] = all_stars
    
    # Cria um grupo somente com os sprites de plataforma.
    # Sprites de plataforma são aqueles que permitem que o jogador passe quando
    # estiver pulando, mas pare quando estiver caindo.
    platforms = pygame.sprite.Group()

    # Criando os meteoros
    for i in range(5):
        meteor = Meteor(assets)
        all_sprites.add(meteor)
        all_meteors.add(meteor)

    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador, independente
    # de onde ele está vindo

    # Cria Sprite do jogador
    player_sun = Sun(assets[SUN_IMG], 11, 0, platforms) #Sol
    player_moon = Moon(assets[MOON_IMG], 11, 1, platforms) #Lua

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == PLATF:
                    platforms.add(tile)

                    # chance de colocar estrela em cima da plataforma
                    if random.random() < 0.25:
                        star = Star(assets['star_img'], row, column)
                        all_sprites.add(star)
                        all_stars.add(star)

    # Adiciona o jogador no grupo de sprites por último para ser desenhado por cima das plataformas
    all_sprites.add(player_sun)
    all_sprites.add(player_moon)

    DONE = 0
    PLAYING = 1
    EXPLODING_MOON = 2
    EXPLODING_SUN = 3
    TRANSITION = 4
    state = PLAYING

    keys_down = {}
    score_moon = 0
    score_sun = 0
    lives_moon = 3
    lives_sun = 3

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

        if state == PLAYING:
                
            if player_moon.rect.y > HEIGHT and lives_moon > 0:
                lives_moon -= 1
                player_moon.reset_position_moon()

            if player_sun.rect.y > HEIGHT and lives_sun > 0:
                lives_sun -= 1
                player_sun.reset_position_sun()

            # Verifica se houve colisão entre LUA e meteoro
            hits = pygame.sprite.spritecollide(player_moon, all_meteors, True, pygame.sprite.collide_mask)
            for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                #assets['destroy_sound'].play()
                m = Meteor(assets)
                all_sprites.add(m)
                all_meteors.add(m)

            if len(hits) > 0:
                # Toca o som da colisão
                #assets['boom_sound'].play()
                player_moon.kill()
                lives_moon -= 1
                explosao = Explosion(player_moon.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING_MOON
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
            
            #Verifica se o jogador LUA pegou a estrela
            moon_hits = pygame.sprite.spritecollide(player_moon, all_stars, True)
            for star in moon_hits:
                score_moon += 1
                #assets['star_sound'].play()

            # Verifica se houve colisão entre SOL e meteoro
            hits = pygame.sprite.spritecollide(player_sun, all_meteors, True, pygame.sprite.collide_mask)
            for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                #assets['destroy_sound'].play()
                m = Meteor(assets)
                all_sprites.add(m)
                all_meteors.add(m)
            
            #Verifica se o jogador SOL pegou a estrela
            star_hits = pygame.sprite.spritecollide(player_sun, all_stars, True)
            for star in star_hits:
                score_sun += 1
                #assets['star_sound'].play()

            if len(hits) > 0:
                # Toca o som da colisão
                #assets['boom_sound'].play()
                player_sun.kill()
                lives_sun -= 1
                explosao = Explosion(player_sun.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING_SUN
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400

        elif state == EXPLODING_MOON:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives_moon == 0:
                    state = TRANSITION 
                    #exibir imagem que sol ganhou 
                else:
                    state = PLAYING
                    player_moon = Moon(assets[MOON_IMG], 11, 1, platforms) #Lua
                    all_sprites.add(player_moon)
        elif state == EXPLODING_SUN:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives_sun == 0:
                    state = TRANSITION 
                    #exibir imagem que lua ganhou 
                else:
                    state = PLAYING
                    player_sun = Sun(assets[SUN_IMG], 11, 0, platforms) #Sol
                    all_sprites.add(player_sun)
        

        # A cada loop, redesenha o fundo e os sprites
        window.blit(background, (0, 0))
        all_sprites.draw(window)

        # ----- Gera saídas

        # Desenhando as vidas da lua
        text_surface = assets['score_font'].render(chr(9829) * lives_moon, True, (200,200,200))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas do sol
        text_surface = assets['score_font'].render(chr(9829) * lives_sun, True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomright = (WIDTH - 10, HEIGHT - 10)
        window.blit(text_surface, text_rect)  

        # Desenhando a pontuação da lua
        text_surface = assets['score_font'].render("LUA: " + str(score_moon), True, (200,200,200))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        window.blit(text_surface, text_rect)

        # Desenhando a pontuação do sol
        text_surface = assets['score_font'].render("SOL: " + str(score_sun), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.topright = (WIDTH - 10, 10)
        window.blit(text_surface, text_rect) 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
 

        
        # tela_texto = assets['font_media'].render("Tela com o seu jogo", True, WHITE)
        # text_rect = tela_texto.get_rect()
        # text_rect.centerx = WIDTH / 2
        # text_rect.centery = 200
        # window.blit(tela_texto, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
