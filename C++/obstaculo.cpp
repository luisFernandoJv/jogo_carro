#include <iostream>
#include <cstdlib>
#include <ctime>

class Obstaculo {
public:
    Obstaculo(int nivel, int largura, int altura_obstaculo, int largura_obstaculo, int velocidade) {
        x = std::rand() % (largura - largura_obstaculo);
        y = -altura_obstaculo;
        this->largura_obstaculo = largura_obstaculo;
        this->altura_obstaculo = altura_obstaculo;
        tipo = "normal"; // Simplificado para 'normal'
        this->velocidade = velocidade;
    }

    void mostrar() {
        // Espaço reservado para mostrar o obstáculo
        std::cout << "Mostrando o obstáculo..." << std::endl;
    }

    void mover() {
        y += velocidade;
    }

    bool fora_da_tela(int altura) {
        return y > altura;
    }

private:
    int x, y;
    int largura_obstaculo, altura_obstaculo;
    std::string tipo;
    int velocidade;
};
