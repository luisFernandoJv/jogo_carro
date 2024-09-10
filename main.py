import pygame
from score import Score
from fundo import Fundo
from carro import Carro
from obstaculo import Obstaculo, Lento
from poder import Poder, Newpoder

pygame.init()

largura = 400
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Carro")

velocidade = 5
largura_carro = 50
altura_carro = 100
largura_obstaculo = 50
altura_obstaculo = 50
largura_poder = 50
altura_poder = 50
aumento_velocidade = 2
jogo_ativo = True
game_over = False
escudo = False

pygame.mixer.music.set_volume(0.3)
musica_fundo = pygame.mixer.music.load('assets/aud/trilha sonora do game - lady-of-the.mp3')
pygame.mixer.music.play(-1)

barulho_poder = pygame.mixer.Sound('assets/aud/smw_coin.wav')
barulho_poder.set_volume(0.9)

carro_imagem = pygame.image.load('assets/image/carro.png')
carro_imagem = pygame.transform.scale(carro_imagem, (largura_carro, altura_carro))

obstaculo_imagem = pygame.image.load('assets/image/obt.png')
obstaculo_imagem = pygame.transform.scale(obstaculo_imagem, (largura_obstaculo, altura_obstaculo))

lento_imagem = pygame.image.load('assets/image/lento.png')
lento_imagem = pygame.transform.scale(lento_imagem, (largura_obstaculo, altura_obstaculo))

poder_imagem = pygame.image.load('assets/image/escudo.png')
poder_imagem = pygame.transform.scale(poder_imagem, (largura_poder, altura_poder))

new_poder_imagem = pygame.image.load('assets/image/new.png')
new_poder_imagem = pygame.transform.scale(new_poder_imagem, (largura_poder, altura_poder))

carro = Carro(largura, altura, largura_carro, altura_carro, velocidade)
obstaculos = []
poderes = []
new_poderes = [] 
score = Score()
fundo = Fundo(largura, altura)

clock = pygame.time.Clock()
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                carro.direcao = -1
            elif event.key == pygame.K_RIGHT:
                carro.direcao = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                carro.direcao = 0
        elif event.type == pygame.USEREVENT:
            score.mensagem_nivel = False
            pygame.time.set_timer(pygame.USEREVENT, 0)

    fundo.desenhar(tela)
    carro.mostrar(tela, carro_imagem, escudo)
    carro.mover(largura)


    if pygame.time.get_ticks() % max(30, 60 - score.nivel * 10) == 0:
        if score.nivel % 2 == 0: 
            obstaculos.append(Lento(score.nivel, largura, altura_obstaculo, largura_obstaculo, velocidade))
            obstaculos.append(Obstaculo(score.nivel, largura, altura_obstaculo, largura_obstaculo, velocidade))
        else:
            obstaculos.append(Obstaculo(score.nivel, largura, altura_obstaculo, largura_obstaculo, velocidade))

    if len(poderes) < score.nivel:
        poderes.append(Poder(largura, altura_poder, largura_poder, velocidade))

    if len(new_poderes) < (score.nivel // 2):
        new_poderes.append(Newpoder(largura, altura_poder, largura_poder, velocidade, aumento_velocidade))

    for obstaculo in obstaculos[:]:
        if obstaculo.tipo == 'lento':
            obstaculo.mostrar(tela, lento_imagem)
        else:
            obstaculo.mostrar(tela, obstaculo_imagem)
        obstaculo.mover()
        if obstaculo.colidir(carro):
            if escudo:  
                obstaculos.remove(obstaculo)  
                escudo = False  
            else:
                if obstaculo.tipo == 'lento':
                    obstaculo.efeito(carro)
                else:
                    jogo_ativo = False
                    game_over = True
        elif obstaculo.fora_da_tela(altura):
            obstaculos.remove(obstaculo)
            score.aumentar_pontuacao()

    for poder in poderes[:]:
        poder.mostrar(tela, poder_imagem)
        poder.mover()
        if poder.colidir(carro):
            barulho_poder.play()
            poderes.remove(poder)
            escudo = True
        elif poder.fora_da_tela(altura):
            poderes.remove(poder)

    for new_poder in new_poderes[:]:
        new_poder.mostrar(tela, new_poder_imagem)
        new_poder.mover()
        if new_poder.colidir(carro):
            barulho_poder.play()
            new_poderes.remove(new_poder)
            new_poder.aplicar_efeito(carro) 
        elif new_poder.fora_da_tela(altura):
            new_poderes.remove(new_poder)

    velocidade = score.verificar_nivel(velocidade)
    score.mostrar_pontuacao_nivel(tela, largura, altura)

    pygame.display.flip()
    clock.tick(60)

    if game_over:
        score.mostrar_game_over(tela, largura, altura)
        jogo_ativo = False

pygame.quit()
