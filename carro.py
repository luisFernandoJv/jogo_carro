import pygame

class Carro:
    def __init__(self, largura, altura, largura_carro, altura_carro, velocidade):
        self.x = largura // 2 - largura_carro // 2
        self.y = altura - altura_carro - 10
        self.direcao = 0
        self.largura_carro = largura_carro
        self.altura_carro = altura_carro
        self.velocidade = velocidade
        self.velocidade_lateral = 0  # movimento lateral suavizado
        self.trail = []              # rastro visual do carro
        self.invencivel = 0          # frames de invencibilidade após levar dano
        self.piscar = 0              # controle de piscar

    def mostrar(self, tela, carro_imagem, escudo):
        # Rastro de movimento
        for i, (tx, ty, alpha) in enumerate(self.trail):
            surf = carro_imagem.copy()
            surf.set_alpha(alpha)
            tela.blit(surf, (tx, ty))

        # Piscar quando invencível (após colisão com 'lento')
        if self.invencivel > 0:
            self.piscar += 1
            if self.piscar % 6 < 3:  # pisca a cada 3 frames
                return
        else:
            self.piscar = 0

        tela.blit(carro_imagem, (self.x, self.y))

        # Escudo visual
        if escudo:
            t = pygame.time.get_ticks()
            cor_r = int(127 + 127 * abs(__import__('math').sin(t * 0.005)))
            cor_b = int(127 + 127 * abs(__import__('math').cos(t * 0.005)))
            pygame.draw.ellipse(
                tela,
                (cor_r, 80, cor_b),
                (self.x - 8, self.y - 8, self.largura_carro + 16, self.altura_carro + 16),
                3
            )
            pygame.draw.ellipse(
                tela,
                (255, 255, 255, 80),
                (self.x - 4, self.y - 4, self.largura_carro + 8, self.altura_carro + 8),
                1
            )

    def mover(self, largura):
        # Aceleração lateral suave
        aceleracao = 1.5
        friccao = 0.75

        if self.direcao != 0:
            self.velocidade_lateral += self.direcao * aceleracao
        else:
            self.velocidade_lateral *= friccao

        # Limitar velocidade lateral
        max_lateral = self.velocidade * 1.2
        self.velocidade_lateral = max(-max_lateral, min(self.velocidade_lateral, max_lateral))

        self.x += self.velocidade_lateral
        self.x = max(50, min(self.x, largura - 50 - self.largura_carro))

        # Atualizar rastro
        self.trail.append((self.x, self.y, 60))
        if len(self.trail) > 5:
            self.trail.pop(0)
        # Diminuir alpha do rastro
        self.trail = [(tx, ty, max(0, a - 12)) for tx, ty, a in self.trail]

        # Decrementar invencibilidade
        if self.invencivel > 0:
            self.invencivel -= 1