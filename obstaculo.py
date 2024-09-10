import pygame
import random
class Obstaculo:
    def __init__(self, nivel, largura, altura_obstaculo, largura_obstaculo, velocidade):
        self.x = random.randint(0, largura - largura_obstaculo)
        self.y = -altura_obstaculo
        self.largura_obstaculo = largura_obstaculo
        self.altura_obstaculo = altura_obstaculo
        self.tipo = random.choice(['normal', 'duplo', 'triplo', 'game_over']) if nivel > 1 else 'normal'
        self.velocidade = random.randint(velocidade, velocidade + 3) if nivel > 2 else velocidade

    def mostrar(self, tela, obstaculo_imagem, game_over_imagem=None):
        if self.tipo == 'normal':
            tela.blit(obstaculo_imagem, (self.x, self.y))
        elif self.tipo == 'duplo':
            tela.blit(obstaculo_imagem, (self.x, self.y))
            tela.blit(obstaculo_imagem, (self.x + self.largura_obstaculo + 10, self.y))
        elif self.tipo == 'triplo':
            tela.blit(obstaculo_imagem, (self.x, self.y))
            tela.blit(obstaculo_imagem, (self.x + self.largura_obstaculo + 10, self.y))
            tela.blit(obstaculo_imagem, (self.x + 2 * (self.largura_obstaculo + 10), self.y))
        elif self.tipo == 'game_over' and game_over_imagem:
            tela.blit(game_over_imagem, (self.x, self.y))

    def mover(self):
        self.y += self.velocidade

    def fora_da_tela(self, altura):
        return self.y > altura

    def colidir(self, carro):
        if self.tipo == 'normal':
            return not (carro.x + carro.largura_carro < self.x or carro.x > self.x + self.largura_obstaculo or carro.y > self.y + self.altura_obstaculo or carro.y + carro.altura_carro < self.y)
        elif self.tipo == 'duplo':
            return not (carro.x + carro.largura_carro < self.x or carro.x > self.x + 2 * self.largura_obstaculo + 10 or carro.y > self.y + self.altura_obstaculo or carro.y + carro.altura_carro < self.y)
        elif self.tipo == 'triplo':
            return not (carro.x + carro.largura_carro < self.x or carro.x > self.x + 3 * self.largura_obstaculo + 20 or carro.y > self.y + self.altura_obstaculo or carro.y + carro.altura_carro < self.y)
        elif self.tipo == 'lento':
            return not (carro.x + carro.largura_carro < self.x or carro.x > self.x + self.largura_obstaculo or carro.y > self.y + self.altura_obstaculo or carro.y + carro.altura_carro < self.y)
        elif self.tipo == 'game_over':
            return not (carro.x + carro.largura_carro < self.x or carro.x > self.x + self.largura_obstaculo or carro.y > self.y + self.altura_obstaculo or carro.y + carro.altura_carro < self.y)

class Lento(Obstaculo):
    def __init__(self, nivel, largura, altura_obstaculo, largura_obstaculo, velocidade):
        super().__init__(nivel, largura, altura_obstaculo, largura_obstaculo, velocidade)
        self.tipo = 'lento'
    
    def mostrar(self, tela, lento_imagem):
        tela.blit(lento_imagem, (self.x, self.y))
        
    def efeito(self, carro):
        carro.velocidade = max(carro.velocidade - 10, 1) 
