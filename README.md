# 🏎️ Pista Turbulenta — Pygame Racing Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/Pygame-2D2D2D?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Herança%20%26%20Polimorfismo-blue?style=for-the-badge)
![Java](https://img.shields.io/badge/Foco-Backend%20Java-red?style=for-the-badge&logo=openjdk&logoColor=white)

<br>

**Projeto desenvolvido para consolidar princípios de POO — os mesmos pilares que aplico diariamente no ecossistema Java/Spring.**

[Sobre o Projeto](#-sobre-o-projeto) • [Arquitetura](#️-arquitetura-e-decisões-técnicas) • [Paralelo com Java](#-paralelo-com-java) • [Como Rodar](#-como-rodar)

<br>

<table>
  <tr>
    <td><img width="300" alt="Gameplay 1" src="https://github.com/user-attachments/assets/2510bea9-cc52-4ff9-b158-2984dbf68461" /></td>
    <td><img width="300" alt="Gameplay 2" src="https://github.com/user-attachments/assets/207d5b82-66e5-4b3f-866d-31b34f7b2bbf" /></td>
  </tr>
</table>

</div>

---

## 🧐 Sobre o Projeto

**Pista Turbulenta** é um jogo 2D de corrida arcade desenvolvido em Python com `pygame`.

O projeto nasceu com um objetivo claro: **praticar os fundamentos de Orientação a Objetos fora do contexto Java**, validando que esses conceitos são universais — não dependem de linguagem. O jogador desvia de obstáculos, coleta power-ups e enfrenta dificuldade crescente conforme avança de nível.

> 💡 **Por que Python/Pygame se meu foco é Java?**
> Porque dominar POO em contextos diferentes — sem o suporte do Spring ou de um framework robusto — demonstra que o conhecimento é genuíno, não memorizado.

---

## 🏗️ Arquitetura e Decisões Técnicas

O código é **totalmente modularizado**, com cada responsabilidade isolada em sua própria classe:

```
jogo_carro/
├── main.py          # Game loop, spawn logic, gerenciamento de estado
├── carro.py         # Entidade do jogador: movimento, colisão, efeitos visuais
├── obstaculo.py     # Hierarquia de obstáculos com comportamentos distintos
├── poder.py         # Hierarquia de power-ups e aplicação de efeitos
├── score.py         # HUD, progressão de nível e tela de game over
└── fundo.py         # Renderização da pista com scroll animado
```

### Padrões aplicados

| Conceito | Como foi aplicado |
|---|---|
| **Herança** | `Lento` e `ZeroCombustivel` estendem `Obstaculo`; `Newpoder` e `Combustivel` estendem `Poder` |
| **Polimorfismo** | `mostrar()` e `efeito()` sobrescritos em cada subclasse — o game loop não precisa saber o tipo concreto |
| **Encapsulamento** | Cada classe gerencia seu próprio estado interno (posição, velocidade, timer) |
| **SRP** | Uma classe, uma responsabilidade — `Score` não mexe em física; `Carro` não sabe do placar |
| **Event-driven** | Spawn de obstáculos e power-ups via `pygame.USEREVENT` — desacoplado do game loop |

---

## ☕ Paralelo com Java

Os mesmos conceitos deste projeto são aplicados no meu dia a dia com Java:

```
Python (aqui)              →  Java / Spring Boot
──────────────────────────────────────────────────
class Obstaculo            →  abstract class / interface
class Lento(Obstaculo)     →  class LentoObstaculo extends Obstaculo
def efeito(self, carro)    →  @Override void aplicarEfeito(Carro carro)
game loop com eventos      →  event-driven com @EventListener / Kafka
modularização por arquivo  →  separação por pacotes (domain, service, infra)
```

---

## 🎮 Controles

| Tecla | Ação |
|:---:|:---|
| `← →` | Mover o carro |
| `ESC` | Voltar ao menu |
| `ENTER / ESPAÇO` | Iniciar jogo |

### Power-ups

| Ícone | Efeito |
|:---:|:---|
| 🛡️ Escudo | Protege de uma colisão fatal |
| ⚡ Turbo | Aumenta a velocidade do carro |
| ⛽ Combustível | Aplica boost aleatório de velocidade |

---

## 🚀 Como Rodar

**Pré-requisitos:** Python 3.8+

```bash
# 1. Clone o repositório
git clone https://github.com/luisFernandoJv/jogo_carro.git
cd jogo_carro

# 2. Instale a dependência
pip install pygame

# 3. Execute
python main.py
```

---

## 🛠️ Stack & Conhecimentos Demonstrados

Esse projeto é parte de um portfólio mais amplo que inclui:

- **Backend Java** — Spring Boot, Spring Data JPA, APIs REST, autenticação JWT
- **Banco de Dados** — PostgreSQL, MySQL, consultas otimizadas, modelagem relacional
- **POO Avançado** — Herança, polimorfismo, interfaces, SOLID
- **Python** — Scripts, automação, desenvolvimento de jogos com pygame
- **Ferramentas** — Git, Maven/Gradle, IntelliJ, VS Code

---

## 📬 Contato

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/luisfernando-eng)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:luizfer.12321@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/luisFernandoJv)

</div>
