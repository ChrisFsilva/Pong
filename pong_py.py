# PONG 
import pygame

pygame.init()
janela =  pygame.display.set_mode([500,500])

# Cores do display
BG_Ground = (107, 142, 35) 
PRETO = (0,0,0)

# Posições iniciais
# Posição da raquete 2
raquete1_x, raquete1_y = 10, 225

# Posição da raquete 2
raquete2_x, raquete2_y = 470,225

# Posição da bola
bola_x,bola_y = 250,250

# Velocidade inicial das raquetes
velocidade_raquete = 0.3

# velocidade da bola da bola
velocidade_bola_x,velocidade_bola_y = 0.1, 0.1

# Medida das raquetes
raquete_largura, raquete_altura = 20,100

# Medida da bola
bola_largura, bola_altura = 20,20

# Placares iniciais
placar1 = 0
placar2 = 0

# Definição de fonte
font = pygame.font.SysFont(None,55)

# Desenhar display
def desenhar():
    # Cor da Janela Braca
    janela.fill(BG_Ground)
    # Cor da raquete 1
    pygame.draw.rect(janela, PRETO, (raquete1_x,raquete1_y,raquete_largura,raquete_altura))
    # Cor da raquete 2
    pygame.draw.rect(janela, PRETO, (raquete2_x,raquete2_y,raquete_largura,raquete_altura))
    # Cor da bola
    pygame.draw.ellipse(janela, PRETO, (bola_x,bola_y,bola_largura, bola_altura))
    
    # Cor do placara
    placar_texto = font.render(f'{placar1} | {placar2}', True, PRETO)

    janela.blit(placar_texto, (200,20))


loop = True

# Looping que rodará o jogo
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    keys = pygame.key.get_pressed()

# Movimento Raquete 1
    if keys[pygame.K_w] and raquete1_y > 10:
        raquete1_y -= velocidade_raquete
    
    if keys[pygame.K_s] and raquete1_y < 490 - raquete_altura:
        raquete1_y += velocidade_raquete

# Movimento Raquete 2
    if keys[pygame.K_UP] and raquete2_y > 10:
        raquete2_y -= velocidade_raquete
    
    if keys[pygame.K_DOWN] and raquete2_y < 490 - raquete_altura:
        raquete2_y += velocidade_raquete

# Velocidade da bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

# Impedir a bola de sair

    if bola_y <= 0 or bola_y >= 498 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

# Colisão

    # Colisão da raquete 1
    if (raquete1_x < bola_x < raquete1_x + raquete_largura) and (raquete1_y < bola_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x


    # Colisão da raquete 2
    if (raquete2_x-10 < bola_x < raquete2_x + raquete_largura) and (raquete2_y < bola_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x

    
# Pontuação
# Jogador 1
    if bola_x <= 0:
        placar2 += 1
        bola_x, bola_y = 250,250

# Jogador 2
    if bola_x >= 500:
        placar1 += 1
        bola_x, bola_y = 250,250

    desenhar()

    pygame.display.update()