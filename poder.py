import random

class Poder:
    def __init__(self, largura, altura_poder, largura_poder, velocidade):
        self.x = random.randint(0, largura - largura_poder)
        self.y = -altura_poder
        self.largura_poder = largura_poder
        self.altura_poder = altura_poder
        self.velocidade = velocidade

    def mostrar(self, tela, poder_imagem):
        tela.blit(poder_imagem, (self.x, self.y))

    def mover(self):
        self.y += self.velocidade

    def fora_da_tela(self, altura):
        return self.y > altura

    def colidir(self, carro):
        return not (carro.x + carro.largura_carro < self.x or carro.x > self.x + self.largura_poder or carro.y > self.y + self.altura_poder or carro.y + carro.altura_carro < self.y)
