import pygame
from score import Score
from fundo import Fundo
from carro import Carro
from obstaculo import Obstaculo
from poder import Poder

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

obstaculo_imagem = pygame.image.load('assets/image/obstaculo.png')
obstaculo_imagem = pygame.transform.scale(obstaculo_imagem, (largura_obstaculo, altura_obstaculo))

poder_imagem = pygame.image.load('assets/image/poder.png')
poder_imagem = pygame.transform.scale(poder_imagem, (largura_poder, altura_poder))

new_poder = pygame.image.load('assets/image/new.png')
new_poder = pygame.transform.scale(new_poder, (largura_poder, altura_poder))


carro = Carro(largura, altura, largura_carro, altura_carro, velocidade)
obstaculos = []
poderes = []
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
        obstaculos.append(Obstaculo(score.nivel, largura, altura_obstaculo, largura_obstaculo, velocidade))

    if len(poderes) < score.nivel:
        poderes.append(Poder(largura, altura_poder, largura_poder, velocidade))

    for obstaculo in obstaculos[:]:
        obstaculo.mostrar(tela, obstaculo_imagem)
        obstaculo.mover()
        if obstaculo.colidir(carro):
            if escudo:
                obstaculos.remove(obstaculo)
                escudo = False
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

    velocidade = score.verificar_nivel(velocidade)
    score.mostrar_pontuacao_nivel(tela, largura, altura)

    pygame.display.flip()
    clock.tick(60)

    if game_over:
        score.mostrar_game_over(tela, largura, altura)
        jogo_ativo = False

pygame.quit()
