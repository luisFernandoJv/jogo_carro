import pygame

class Carro:
    def __init__(self, width, height, largura_carro, altura_carro, velocidade):
        self.x = width // 2 - largura_carro // 2
        self.y = height - altura_carro - 10
        self.direcao = 0
        self.largura_carro = largura_carro
        self.altura_carro = altura_carro
        self.velocidade = velocidade

    def mostrar(self, tela, carro_imagem, escudo):
        tela.blit(carro_imagem, (self.x, self.y))
        if escudo:
            pygame.draw.rect(tela, (255, 0, 255), (self.x - 5, self.y - 5, self.largura_carro + 10, self.altura_carro + 10), 4)

    def mover(self, width):
        self.x += self.direcao * self.velocidade
        self.x = max(0, min(self.x, width - self.largura_carro))
