# 🏎️ Pista Turbulenta - Pygame Racing

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/pygame-2D2D2D?style=for-the-badge&logo=pygame&logoColor=white)
![POO](https://img.shields.io/badge/POO-Design%20Patterns-blue?style=for-the-badge)

<br>

**Um jogo de corrida arcade desenvolvido em Python focado em lógica de colisão e orientação a objetos.**

[🧐 Sobre](#-sobre-o-projeto) • [🚀 Instalação](#-como-rodar) • [🛠️ Tecnologias](#-tecnologias)

<br>

<img src="https://github.com/user-attachments/assets/ffd3ac90-16cb-411f-a25e-39e42fe31301" alt="Gameplay Pista Turbulenta" width="700" style="border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.5);">

</div>

---

## 🧐 Sobre o Projeto

O **Pista Turbulenta** é um jogo 2D desenvolvido com a biblioteca `pygame` para demonstrar conceitos práticos de desenvolvimento de jogos e Programação Orientada a Objetos (POO).

O jogador controla um carro em uma rodovia movimentada, desviando de obstáculos, coletando combustíveis e power-ups (escudos) para sobreviver o maior tempo possível. A dificuldade aumenta progressivamente conforme a pontuação sobe.

### 🎮 Destaques de Engenharia
- **Sistema de Classes:** Código modularizado (`Carro`, `Obstaculo`, `Poder`, `Score`) para facilitar a manutenção.
- **Herança e Polimorfismo:** Classes `Lento` e `ZeroCombustivel` herdam de `Obstaculo` com comportamentos distintos.
- **Gerenciamento de Colisão:** Lógica precisa para detecção de impacto e aplicação de efeitos (Game Over, Lentidão ou Escudo).
- **Progressão de Dificuldade:** Algoritmo que ajusta a velocidade e a frequência de spawn dos inimigos com base no nível atual.

---

## 🕹️ Controles

| Tecla | Ação |
| :---: | :--- |
| **⬅️ Seta Esquerda** | Move o carro para a esquerda |
| **➡️ Seta Direita** | Move o carro para a direita |
| **Escudo (Power-up)** | Protege contra uma colisão |

---

## 🚀 Como Rodar

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado em sua máquina.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/luisFernandoJv/jogo_carro.git](https://github.com/luisFernandoJv/jogo_carro.git)
   cd jogo_carro
