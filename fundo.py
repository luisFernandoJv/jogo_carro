import pygame

class Fundo:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def desenhar(self, tela):
        tela.fill((47, 79, 47))
        pygame.draw.rect(tela, (190, 190, 190), (50, 0, self.width - 100, self.height))

        pygame.draw.line(tela, (255, 255, 255), (50, 0), (50, self.height), 5)
        pygame.draw.line(tela, (255, 255, 255), (self.width - 50, 0), (self.width - 50, self.height), 5)

        for i in range(0, self.height, 40):
            pygame.draw.line(tela, (255, 255, 0), (self.width // 2, i), (self.width // 2, i + 20), 5)
