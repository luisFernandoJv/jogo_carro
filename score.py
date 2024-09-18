import pygame

class Score:
    def __init__(self):
        self.pontuacao = 0
        self.nivel = 1
        self.mensagem_nivel = False
        self.tempo_mensagem = 0

    def mostrar_pontuacao_nivel(self, tela, largura, altura):
        fonte = pygame.font.Font(None, 30) 
        texto_pontuacao = fonte.render(f"Pontuação: {self.pontuacao}", True, (255, 255, 255))
        texto_nivel = fonte.render(f"Nível: {self.nivel}", True, (255, 255, 255))

        largura_telinha = max(texto_pontuacao.get_width(), texto_nivel.get_width()) + 10
        altura_telinha = texto_pontuacao.get_height() + texto_nivel.get_height() + 10

     
        pygame.draw.rect(tela, (0, 0, 0), (largura - largura_telinha - 10, 10, largura_telinha, altura_telinha))
        pygame.draw.rect(tela, (255, 255, 255), (largura - largura_telinha - 10, 10, largura_telinha, altura_telinha), 1)

        tela.blit(texto_pontuacao, (largura - largura_telinha - 5, 15))
        tela.blit(texto_nivel, (largura - largura_telinha - 5, 40))

        if self.mensagem_nivel:
            if pygame.time.get_ticks() - self.tempo_mensagem < 3000:
                texto_mensagem = fonte.render(f"Parabéns! Fase {self.nivel}", True, (255, 0, 0))
                tela.blit(texto_mensagem, (largura // 2 - texto_mensagem.get_width() // 2, altura // 2 - texto_mensagem.get_height() // 2))
            else:
                self.mensagem_nivel = False

    def aumentar_pontuacao(self):
        self.pontuacao += 1

    def verificar_nivel(self, velocidade):
        if self.pontuacao >= self.nivel * 50:
            self.nivel += 1
            velocidade += 1
            self.mensagem_nivel = True
            self.tempo_mensagem = pygame.time.get_ticks()
        return velocidade

    def mostrar_game_over(self, tela, largura, altura):
        tela.fill((255, 255, 255))
        fonte = pygame.font.Font(None, 100)
        texto_game_over = fonte.render("Game Over", True, (255, 0, 0))
        tela.blit(texto_game_over, (largura // 2 - texto_game_over.get_width() // 2, altura // 2 - texto_game_over.get_height() // 2))

        fonte_pequena = pygame.font.Font(None, 50)
        texto_pontuacao_final = fonte_pequena.render(f"Pontuação Final: {self.pontuacao}", True, (0, 0, 0))
        tela.blit(texto_pontuacao_final, (largura // 2 - texto_pontuacao_final.get_width() // 2, altura // 2 + 50))

        texto_nivel_final = fonte_pequena.render(f"Nível Atingido: {self.nivel}", True, (255, 0, 0))
        tela.blit(texto_nivel_final, (largura // 2 - texto_nivel_final.get_width() // 2, altura // 2 + 90))

        pygame.display.flip()
        pygame.time.wait(3000)
