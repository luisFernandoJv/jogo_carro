#include <iostream>

class Carro {
public:
    Carro(int largura, int altura, int largura_carro, int altura_carro, int velocidade)
        : largura(largura), altura(altura), largura_carro(largura_carro),
          altura_carro(altura_carro), velocidade(velocidade) {
        x = largura / 2 - largura_carro / 2;
        y = altura - altura_carro - 10;
        direcao = 0;
    }

    void mostrar() {

        std::cout << "Mostrando o carro..." << std::endl;
    }

    void mover() {
        x += direcao * velocidade;
        if (x < 0) x = 0;
        if (x > largura - largura_carro) x = largura - largura_carro;
    }

    void setDirecao(int nova_direcao) {
        direcao = nova_direcao;
    }

private:
    int x, y;
    int direcao;
    int largura, altura;
    int largura_carro, altura_carro;
    int velocidade;
};
