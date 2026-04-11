import pygame


class Score:
    def __init__(self):
        self.pontuacao = 0
        self.nivel = 1
        self.mensagem_nivel = False
        self.tempo_mensagem = 0
        self.combo = 0
        self.ultimo_desvio = 0
        self._particulas_hud = []

    # ─── HUD principal ───────────────────────────────────────────────────────
    def mostrar_pontuacao_nivel(self, tela, largura, altura):
        # Fonte
        try:
            fonte_hud = pygame.font.SysFont("consolas", 22, bold=True)
            fonte_sub = pygame.font.SysFont("consolas", 16)
        except Exception:
            fonte_hud = pygame.font.Font(None, 26)
            fonte_sub = pygame.font.Font(None, 20)

        # Painel HUD semi-transparente no topo
        painel = pygame.Surface((150, 70), pygame.SRCALPHA)
        painel.fill((0, 0, 0, 160))
        pygame.draw.rect(painel, (255, 255, 0, 180), (0, 0, 150, 70), 1)
        tela.blit(painel, (largura - 160, 10))

        # Pontuação
        txt_pts = fonte_hud.render(f"PTS {self.pontuacao:05d}", True, (255, 220, 0))
        tela.blit(txt_pts, (largura - 155, 18))

        # Nível com barra de progresso
        txt_nv = fonte_sub.render(f"NÍVEL {self.nivel}", True, (200, 200, 200))
        tela.blit(txt_nv, (largura - 155, 44))

        # Barra de progresso para próximo nível
        progresso = min((self.pontuacao % (self.nivel * 50)) / (self.nivel * 50), 1.0)
        pygame.draw.rect(tela, (60, 60, 60), (largura - 155, 60, 140, 8), border_radius=4)
        pygame.draw.rect(tela, (255, 180, 0), (largura - 155, 60, int(140 * progresso), 8), border_radius=4)

        # Mensagem de nível novo
        if self.mensagem_nivel:
            elapsed = pygame.time.get_ticks() - self.tempo_mensagem
            if elapsed < 2500:
                alpha = 255
                if elapsed > 1800:
                    alpha = int(255 * (1 - (elapsed - 1800) / 700))
                scale = 1.0 + 0.1 * abs(__import__('math').sin(elapsed * 0.008))

                try:
                    fonte_msg = pygame.font.SysFont("consolas", int(42 * scale), bold=True)
                except Exception:
                    fonte_msg = pygame.font.Font(None, int(50 * scale))

                surf_msg = fonte_msg.render(f"▶ FASE {self.nivel}!", True, (255, 220, 0))
                surf_msg.set_alpha(alpha)
                x = largura // 2 - surf_msg.get_width() // 2
                y = altura // 3

                # Sombra
                sombra = fonte_msg.render(f"▶ FASE {self.nivel}!", True, (100, 60, 0))
                sombra.set_alpha(alpha // 2)
                tela.blit(sombra, (x + 3, y + 3))
                tela.blit(surf_msg, (x, y))
            else:
                self.mensagem_nivel = False

    # ─── Pontuação ────────────────────────────────────────────────────────────
    def aumentar_pontuacao(self):
        self.pontuacao += 1 + (self.nivel // 3)  # bônus de pontos em níveis altos

    # ─── Verificação de nível ─────────────────────────────────────────────────
    def verificar_nivel(self, velocidade):
        if self.pontuacao >= self.nivel * 50:
            self.nivel += 1
            velocidade = min(velocidade + 1, 18)  # cap de velocidade
            self.mensagem_nivel = True
            self.tempo_mensagem = pygame.time.get_ticks()
        return velocidade

    # ─── Tela de Game Over ────────────────────────────────────────────────────
    def mostrar_game_over(self, tela, largura, altura):
        # Fundo escuro gradual
        overlay = pygame.Surface((largura, altura), pygame.SRCALPHA)
        overlay.fill((10, 10, 20, 230))
        tela.blit(overlay, (0, 0))

        try:
            fonte_titulo = pygame.font.SysFont("consolas", 72, bold=True)
            fonte_media  = pygame.font.SysFont("consolas", 30, bold=True)
            fonte_pequena = pygame.font.SysFont("consolas", 22)
        except Exception:
            fonte_titulo  = pygame.font.Font(None, 90)
            fonte_media   = pygame.font.Font(None, 40)
            fonte_pequena = pygame.font.Font(None, 28)

        cy = altura // 2 - 80

        # "GAME OVER"
        for offset, cor in [((3, 3), (180, 0, 0)), ((0, 0), (255, 50, 50))]:
            txt = fonte_titulo.render("GAME OVER", True, cor)
            tela.blit(txt, (largura // 2 - txt.get_width() // 2 + offset[0], cy + offset[1]))

        # Separador
        pygame.draw.line(tela, (255, 80, 80), (largura // 4, cy + 85), (largura * 3 // 4, cy + 85), 2)

        # Pontuação final
        txt_pts = fonte_media.render(f"PONTUAÇÃO: {self.pontuacao}", True, (255, 220, 0))
        tela.blit(txt_pts, (largura // 2 - txt_pts.get_width() // 2, cy + 100))

        # Nível atingido
        txt_nv = fonte_media.render(f"NÍVEL: {self.nivel}", True, (180, 180, 255))
        tela.blit(txt_nv, (largura // 2 - txt_nv.get_width() // 2, cy + 140))

        # Instrução
        t = pygame.time.get_ticks()
        alpha_inst = int(127 + 127 * abs(__import__('math').sin(t * 0.003)))
        txt_inst = fonte_pequena.render("Fechando em 3s...", True, (150, 150, 150))
        txt_inst.set_alpha(alpha_inst)
        tela.blit(txt_inst, (largura // 2 - txt_inst.get_width() // 2, cy + 200))

        pygame.display.flip()
        pygame.time.wait(3000)