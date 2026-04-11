import pygame

class Fundo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.offset = 0           # offset de scroll
        self.velocidade_scroll = 5
        self.particulas = []      # partículas de grama/ambiente
        self._gerar_particulas()

    def _gerar_particulas(self):
        import random
        for _ in range(20):
            lado = 0 if __import__('random').random() < 0.5 else 1
            x = __import__('random').randint(0, 45) if lado == 0 else __import__('random').randint(self.largura - 45, self.largura)
            y = __import__('random').randint(0, self.altura)
            tamanho = __import__('random').randint(2, 5)
            alpha = __import__('random').randint(80, 180)
            self.particulas.append([x, y, tamanho, alpha])

    def atualizar(self, velocidade):
        self.velocidade_scroll = velocidade
        self.offset = (self.offset + self.velocidade_scroll) % 80

        # Mover partículas
        import random
        for p in self.particulas:
            p[1] += self.velocidade_scroll * 0.6
            if p[1] > self.altura:
                lado = 0 if random.random() < 0.5 else 1
                p[0] = random.randint(0, 45) if lado == 0 else random.randint(self.largura - 45, self.largura)
                p[1] = -10
                p[2] = random.randint(2, 5)

    def desenhar(self, tela, velocidade=5):
        self.atualizar(velocidade)

        # Grama dos lados com gradiente simulado
        tela.fill((34, 60, 34))

        # Faixa de grama mais escura nas bordas
        pygame.draw.rect(tela, (28, 52, 28), (0, 0, 55, self.altura))
        pygame.draw.rect(tela, (28, 52, 28), (self.largura - 55, 0, 55, self.altura))

        # Asfalto principal
        pygame.draw.rect(tela, (45, 45, 48), (50, 0, self.largura - 100, self.altura))

        # Linhas laterais brancas (bordas da pista)
        pygame.draw.rect(tela, (220, 220, 220), (50, 0, 5, self.altura))
        pygame.draw.rect(tela, (220, 220, 220), (self.largura - 55, 0, 5, self.altura))

        # Linha central tracejada animada (amarela)
        centro = self.largura // 2
        for i in range(-1, self.altura // 80 + 2):
            y = i * 80 + (self.offset % 80)
            pygame.draw.rect(tela, (255, 220, 0), (centro - 3, y, 6, 45))

        # Partículas de ambiente (pedrinhas, grama)
        for p in self.particulas:
            cor = (50 + p[2] * 5, 90 + p[2] * 5, 50)
            pygame.draw.circle(tela, cor, (int(p[0]), int(p[1])), p[2])

        # Sombra sutil nas bordas do asfalto
        for i in range(8):
            alpha_surf = pygame.Surface((3, self.altura), pygame.SRCALPHA)
            alpha_surf.fill((0, 0, 0, 30 - i * 3))
            tela.blit(alpha_surf, (55 + i, 0))
            tela.blit(alpha_surf, (self.largura - 63 + i, 0))