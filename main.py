import pygame
import random
import math
from score import Score
from fundo import Fundo
from carro import Carro
from obstaculo import Obstaculo, Lento, ZeroCombustivel
from poder import Poder, Newpoder, Combustivel

# ─── Inicialização ─────────────────────────────────────────────────────────
pygame.init()

LARGURA  = 400
ALTURA   = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pista Turbulenta")

# ─── Constantes ────────────────────────────────────────────────────────────
VEL_INICIAL      = 5
LARG_CARRO       = 50
ALT_CARRO        = 100
LARG_OBJ         = 50
ALT_OBJ          = 50
AUMENTO_VEL      = 2

# Timers de spawn (em ms)
TIMER_OBSTACULO  = pygame.USEREVENT + 1
TIMER_PODER      = pygame.USEREVENT + 2
TIMER_NEWPODER   = pygame.USEREVENT + 3
TIMER_COMBUSTIVEL = pygame.USEREVENT + 4

# ─── Áudio ─────────────────────────────────────────────────────────────────
try:
    pygame.mixer.music.load('assets/aud/trilha sonora do game - lady-of-the.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
except Exception:
    pass

try:
    barulho_poder = pygame.mixer.Sound('assets/aud/smw_coin.wav')
    barulho_poder.set_volume(0.9)
except Exception:
    barulho_poder = None

# ─── Imagens ───────────────────────────────────────────────────────────────
def carregar(caminho, w, h):
    img = pygame.image.load(caminho)
    return pygame.transform.scale(img, (w, h))

carro_imagem      = carregar('assets/image/carro.png',       LARG_CARRO, ALT_CARRO)
obstaculo_imagem  = carregar('assets/image/obt.png',         LARG_OBJ, ALT_OBJ)
lento_imagem      = carregar('assets/image/lento.png',       LARG_OBJ, ALT_OBJ)
poder_imagem      = carregar('assets/image/escudo.png',      LARG_OBJ, ALT_OBJ)
new_poder_imagem  = carregar('assets/image/new.png',         LARG_OBJ, ALT_OBJ)
quebra_imagem     = carregar('assets/image/Ob2.png',         LARG_OBJ, ALT_OBJ)
combustivel_imagem= carregar('assets/image/combustivel.png', LARG_OBJ, ALT_OBJ)

# ─── Partículas de explosão / coleta ───────────────────────────────────────
particulas = []

def spawn_particulas(x, y, cor, quantidade=12):
    for _ in range(quantidade):
        ang = random.uniform(0, math.pi * 2)
        vel = random.uniform(2, 6)
        vida = random.randint(20, 40)
        particulas.append({
            'x': x, 'y': y,
            'vx': math.cos(ang) * vel,
            'vy': math.sin(ang) * vel,
            'cor': cor, 'vida': vida, 'max_vida': vida
        })

def atualizar_particulas(tela):
    for p in particulas[:]:
        p['x'] += p['vx']
        p['y'] += p['vy']
        p['vy'] += 0.2  # gravidade leve
        p['vida'] -= 1
        alpha = int(255 * p['vida'] / p['max_vida'])
        raio = max(1, int(4 * p['vida'] / p['max_vida']))
        surf = pygame.Surface((raio * 2, raio * 2), pygame.SRCALPHA)
        cor_a = (*p['cor'], alpha)
        pygame.draw.circle(surf, cor_a, (raio, raio), raio)
        tela.blit(surf, (int(p['x']) - raio, int(p['y']) - raio))
        if p['vida'] <= 0:
            particulas.remove(p)

# ─── Tela de início ────────────────────────────────────────────────────────
def tela_inicio():
    try:
        fonte_titulo = pygame.font.SysFont("consolas", 52, bold=True)
        fonte_sub    = pygame.font.SysFont("consolas", 22)
        fonte_info   = pygame.font.SysFont("consolas", 18)
    except Exception:
        fonte_titulo = pygame.font.Font(None, 60)
        fonte_sub    = pygame.font.Font(None, 30)
        fonte_info   = pygame.font.Font(None, 24)

    fundo_menu = Fundo(LARGURA, ALTURA)
    clock = pygame.time.Clock()
    t = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                return

        fundo_menu.desenhar(tela, VEL_INICIAL)
        t += 1

        # Overlay escuro
        overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        tela.blit(overlay, (0, 0))

        # Título com brilho pulsante
        brilho = int(200 + 55 * abs(math.sin(t * 0.04)))
        titulo = fonte_titulo.render("PISTA", True, (255, brilho, 0))
        sub    = fonte_titulo.render("TURBULENTA", True, (255, brilho, 0))
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 140))
        tela.blit(sub,    (LARGURA // 2 - sub.get_width() // 2, 195))

        # Linha decorativa
        pygame.draw.line(tela, (255, 180, 0), (80, 255), (LARGURA - 80, 255), 2)

        # Instruções
        controles = [
            "← → Mover carro",
            "",
            "🛡  Escudo: protege 1 colisão",
            "⚡ Turbo:  aumenta velocidade",
            "⛽ Fuel:   boost aleatório",
        ]
        for i, linha in enumerate(controles):
            cor = (200, 200, 200) if linha else (100, 100, 100)
            txt = fonte_info.render(linha, True, cor)
            tela.blit(txt, (LARGURA // 2 - txt.get_width() // 2, 275 + i * 28))

        # Botão START piscante
        if (t // 20) % 2 == 0:
            start = fonte_sub.render("[ ENTER ou ESPAÇO ]", True, (255, 255, 100))
            tela.blit(start, (LARGURA // 2 - start.get_width() // 2, 460))

        pygame.display.flip()
        clock.tick(60)

# ─── HUD de ícones de poder ────────────────────────────────────────────────
def mostrar_hud_poderes(tela, escudo, vel_carro):
    try:
        fonte = pygame.font.SysFont("consolas", 16)
    except Exception:
        fonte = pygame.font.Font(None, 20)

    # Velocidade
    barra_w = 80
    barra_h = 10
    proporcao = min(vel_carro / 20, 1.0)
    cor_vel = (
        int(255 * proporcao),
        int(255 * (1 - proporcao)),
        0
    )
    txt_vel = fonte.render(f"VEL {vel_carro}", True, (200, 200, 200))
    tela.blit(txt_vel, (10, 18))
    pygame.draw.rect(tela, (60, 60, 60), (10, 38, barra_w, barra_h), border_radius=5)
    pygame.draw.rect(tela, cor_vel, (10, 38, int(barra_w * proporcao), barra_h), border_radius=5)

    # Escudo ativo
    if escudo:
        t = pygame.time.get_ticks()
        r = int(180 + 75 * abs(math.sin(t * 0.005)))
        b = int(180 + 75 * abs(math.cos(t * 0.005)))
        txt_esc = fonte.render("🛡 ESCUDO", True, (r, 100, b))
        tela.blit(txt_esc, (10, 56))

# ─── Loop principal ────────────────────────────────────────────────────────
def jogo():
    velocidade = VEL_INICIAL
    escudo = False
    game_over = False

    carro     = Carro(LARGURA, ALTURA, LARG_CARRO, ALT_CARRO, velocidade)
    obstaculos = []
    poderes    = []
    new_poderes = []
    combustives = []
    score     = Score()
    fundo     = Fundo(LARGURA, ALTURA)
    clock     = pygame.time.Clock()

    # Timers de spawn em ms (intervalo inicial)
    pygame.time.set_timer(TIMER_OBSTACULO,   1200)
    pygame.time.set_timer(TIMER_PODER,       8000)
    pygame.time.set_timer(TIMER_NEWPODER,   10000)
    pygame.time.set_timer(TIMER_COMBUSTIVEL, 9000)

    jogo_ativo = True
    while jogo_ativo:
        # ── Eventos ──────────────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # encerrar

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    carro.direcao = -1
                elif event.key == pygame.K_RIGHT:
                    carro.direcao = 1
                elif event.key == pygame.K_ESCAPE:
                    return True  # voltar ao menu

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    carro.direcao = 0

            # Spawns por timer
            elif event.type == TIMER_OBSTACULO:
                nivel = score.nivel
                if nivel % 2 == 0:
                    obstaculos.append(ZeroCombustivel(nivel, LARGURA, ALT_OBJ, LARG_OBJ, velocidade))
                    obstaculos.append(Lento(nivel, LARGURA, ALT_OBJ, LARG_OBJ, velocidade))
                obstaculos.append(Obstaculo(nivel, LARGURA, ALT_OBJ, LARG_OBJ, velocidade))
                # Ajustar intervalo com o nível (spawn mais rápido)
                novo_intervalo = max(400, 1200 - score.nivel * 60)
                pygame.time.set_timer(TIMER_OBSTACULO, novo_intervalo)

            elif event.type == TIMER_PODER:
                poderes.append(Poder(LARGURA, ALT_OBJ, LARG_OBJ, velocidade))

            elif event.type == TIMER_NEWPODER and score.nivel >= 2:
                new_poderes.append(Newpoder(LARGURA, ALT_OBJ, LARG_OBJ, velocidade, AUMENTO_VEL))

            elif event.type == TIMER_COMBUSTIVEL and score.nivel >= 2:
                combustives.append(Combustivel(LARGURA, ALT_OBJ, LARG_OBJ, velocidade, AUMENTO_VEL))

        # ── Desenho ───────────────────────────────────────────────────────
        fundo.desenhar(tela, velocidade)
        carro.mostrar(tela, carro_imagem, escudo)
        carro.mover(LARGURA)

        # ── Obstáculos ───────────────────────────────────────────────────
        for obs in obstaculos[:]:
            if isinstance(obs, Lento):
                obs.mostrar(tela, lento_imagem)
            elif isinstance(obs, ZeroCombustivel):
                obs.mostrar(tela, quebra_imagem)
            else:
                obs.mostrar(tela, obstaculo_imagem)

            obs.mover()

            if obs.colidir(carro):
                cx = carro.x + LARG_CARRO // 2
                cy = carro.y + ALT_CARRO // 2
                if escudo:
                    spawn_particulas(cx, cy, (100, 200, 255), 16)
                    obstaculos.remove(obs)
                    escudo = False
                    if barulho_poder:
                        barulho_poder.play()
                else:
                    if isinstance(obs, (Lento, ZeroCombustivel)):
                        if carro.invencivel == 0:
                            obs.efeito(carro)
                            spawn_particulas(cx, cy, (255, 140, 0), 10)
                            obstaculos.remove(obs)
                    else:
                        spawn_particulas(cx, cy, (255, 50, 50), 20)
                        jogo_ativo = False
                        game_over = True

            elif obs.fora_da_tela(ALTURA):
                obstaculos.remove(obs)
                score.aumentar_pontuacao()

        # ── Power-ups ─────────────────────────────────────────────────────
        def processar_poder(lista, imagem, efeito_fn, cor_particula):
            nonlocal escudo
            for p in lista[:]:
                p.mostrar(tela, imagem)
                p.mover()
                if p.colidir(carro):
                    if barulho_poder:
                        barulho_poder.play()
                    spawn_particulas(p.x + LARG_OBJ // 2, p.y + ALT_OBJ // 2, cor_particula, 14)
                    efeito_fn(p)
                    lista.remove(p)
                elif p.fora_da_tela(ALTURA):
                    lista.remove(p)

        def ef_escudo(_p):
            nonlocal escudo
            escudo = True

        processar_poder(poderes,     poder_imagem,     ef_escudo,                  (100, 200, 255))
        processar_poder(new_poderes, new_poder_imagem, lambda p: p.aplicar_efeito(carro), (255, 220, 50))
        processar_poder(combustives, combustivel_imagem, lambda p: p.aplicar_efeito(carro), (255, 120, 30))

        # ── Partículas e HUD ──────────────────────────────────────────────
        atualizar_particulas(tela)
        mostrar_hud_poderes(tela, escudo, carro.velocidade)

        velocidade = score.verificar_nivel(velocidade)
        score.mostrar_pontuacao_nivel(tela, LARGURA, ALTURA)

        pygame.display.flip()
        clock.tick(60)

        if game_over:
            score.mostrar_game_over(tela, LARGURA, ALTURA)
            return True  # voltar ao menu após game over

    return False  # QUIT


# ─── Ponto de entrada ──────────────────────────────────────────────────────
if __name__ == "__main__":
    continuar = True
    while continuar:
        tela_inicio()
        continuar = jogo()

    pygame.quit()