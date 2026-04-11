import pygame
import random


class Obstaculo:
    def __init__(self, nivel, largura, altura_obstaculo, largura_obstaculo, velocidade):
        self.largura_obstaculo = largura_obstaculo
        self.altura_obstaculo = altura_obstaculo
        self.largura = largura
        
        self.tipo = self._sortear_tipo(nivel)
        self.velocidade = random.randint(velocidade, velocidade + 3) if nivel > 2 else velocidade

        # Posição X baseada no tipo (evitar spawnar fora da pista)
        pista_inicio = 55
        pista_fim = largura - 55 - largura_obstaculo
        self.x = random.randint(pista_inicio, max(pista_inicio, pista_fim))
        self.y = -altura_obstaculo

        # Atributo de largura total para colisão genérica
        self.largura = self._largura_total()
        self.altura = altura_obstaculo

        # Efeito visual: shake ao colidir
        self.shake = 0

    def _sortear_tipo(self, nivel):
        if nivel == 1:
            return 'normal'
        opcoes = ['normal', 'duplo', 'triplo']
        pesos   = [50, 30, 20]
        return random.choices(opcoes, weights=pesos, k=1)[0]

    def _largura_total(self):
        if self.tipo == 'duplo':
            return 2 * self.largura_obstaculo + 10
        elif self.tipo == 'triplo':
            return 3 * self.largura_obstaculo + 20
        return self.largura_obstaculo

    def mostrar(self, tela, obstaculo_imagem, *args):
        if self.tipo == 'normal':
            tela.blit(obstaculo_imagem, (self.x, self.y))
        elif self.tipo == 'duplo':
            tela.blit(obstaculo_imagem, (self.x, self.y))
            tela.blit(obstaculo_imagem, (self.x + self.largura_obstaculo + 10, self.y))
        elif self.tipo == 'triplo':
            tela.blit(obstaculo_imagem, (self.x, self.y))
            tela.blit(obstaculo_imagem, (self.x + self.largura_obstaculo + 10, self.y))
            tela.blit(obstaculo_imagem, (self.x + 2 * (self.largura_obstaculo + 10), self.y))

    def mover(self):
        self.y += self.velocidade

    def fora_da_tela(self, altura):
        return self.y > altura

    def colidir(self, carro):
        largura_col = self._largura_total()
        return not (
            carro.x + carro.largura_carro < self.x or
            carro.x > self.x + largura_col or
            carro.y > self.y + self.altura_obstaculo or
            carro.y + carro.altura_carro < self.y
        )


class Lento(Obstaculo):
    """Obstáculo que reduz a velocidade do carro."""

    def __init__(self, nivel, largura, altura_obstaculo, largura_obstaculo, velocidade):
        super().__init__(nivel, largura, altura_obstaculo, largura_obstaculo, velocidade)
        self.tipo = 'lento'

    def mostrar(self, tela, lento_imagem, *args):
        tela.blit(lento_imagem, (self.x, self.y))

    def efeito(self, carro):
        carro.velocidade = max(carro.velocidade - 3, 2)
        carro.invencivel = 60  # 1 segundo de invencibilidade após efeito


class ZeroCombustivel(Obstaculo):
    """Obstáculo que para o carro momentaneamente."""

    def __init__(self, nivel, largura, altura_obstaculo, largura_obstaculo, velocidade):
        super().__init__(nivel, largura, altura_obstaculo, largura_obstaculo, velocidade)
        self.tipo = 'quebra'

    def mostrar(self, tela, quebra_mola_imagem, *args):
        tela.blit(quebra_mola_imagem, (self.x, self.y))

    def efeito(self, carro):
        carro.velocidade = max(carro.velocidade - 2, 1)
        carro.invencivel = 90