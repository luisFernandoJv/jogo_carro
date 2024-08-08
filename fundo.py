import pygame

class Fundo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def desenhar(self, tela):
        tela.fill((47, 79, 47))
        pygame.draw.rect(tela, (190, 190, 190), (50, 0, self.largura - 100, self.altura))

        pygame.draw.line(tela, (255, 255, 255), (50, 0), (50, self.altura), 5)
        pygame.draw.line(tela, (255, 255, 255), (self.largura - 50, 0), (self.largura - 50, self.altura), 5)

        for i in range(0, self.altura, 40):
            pygame.draw.line(tela, (255, 255, 0), (self.largura // 2, i), (self.largura // 2, i + 20), 5)
