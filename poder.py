import random
import pygame


class Poder:
    """Power-up base: escudo."""

    def __init__(self, largura, altura_poder, largura_poder, velocidade):
        pista_inicio = 55
        pista_fim = largura - 55 - largura_poder
        self.x = random.randint(pista_inicio, max(pista_inicio, pista_fim))
        self.y = -altura_poder
        self.largura_poder = largura_poder
        self.altura_poder = altura_poder
        self.velocidade = velocidade
        # Animação de flutuação
        self._offset_base_y = 0.0
        self._tempo = random.uniform(0, 6.28)

    def mostrar(self, tela, imagem):
        import math
        self._tempo += 0.08
        flutuacao = int(math.sin(self._tempo) * 4)
        tela.blit(imagem, (self.x, self.y + flutuacao))

    def mover(self):
        self.y += self.velocidade

    def fora_da_tela(self, altura):
        return self.y > altura

    def colidir(self, carro):
        return not (
            carro.x + carro.largura_carro < self.x or
            carro.x > self.x + self.largura_poder or
            carro.y > self.y + self.altura_poder or
            carro.y + carro.altura_carro < self.y
        )


class Newpoder(Poder):
    """Power-up que aumenta a velocidade do carro."""

    def __init__(self, largura, altura_poder, largura_poder, velocidade, aumento_velocidade):
        super().__init__(largura, altura_poder, largura_poder, velocidade)
        self.aumento_velocidade = aumento_velocidade

    def aplicar_efeito(self, carro):
        carro.velocidade = min(carro.velocidade + self.aumento_velocidade, 20)

    def mostrar(self, tela, imagem):
        super().mostrar(tela, imagem)


class Combustivel(Poder):
    """Power-up que aplica boost de velocidade aleatório."""

    VALORES_BOOST = [1, 2, 3, 4, 5]

    def __init__(self, largura, altura_poder, largura_poder, velocidade, aumento_velocidade):
        super().__init__(largura, altura_poder, largura_poder, velocidade)
        self.aumento_velocidade = aumento_velocidade

    def aplicar_efeito(self, carro):
        boost = random.choice(self.VALORES_BOOST)
        carro.velocidade = min(carro.velocidade + boost, 20)

    def mostrar(self, tela, imagem):
        super().mostrar(tela, imagem)