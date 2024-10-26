#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>

class Obstaculo {
public:
    Obstaculo(int nivel, int largura, int altura_obstaculo, int largura_obstaculo, int velocidade) {
        x = std::rand() % (largura - largura_obstaculo);
        y = -altura_obstaculo;
        this->largura_obstaculo = largura_obstaculo;
        this->altura_obstaculo = altura_obstaculo;
        this->tipo = (nivel > 1) ? randomTipo(nivel) : "normal";
        this->velocidade = (nivel > 2) ? std::rand() % (velocidade + 3 - velocidade) + velocidade : velocidade;
    }

    virtual void mostrar() {
        if (tipo == "normal") {
            std::cout << "Mostrando obstáculo normal na posição (" << x << ", " << y << ")." << std::endl;
        } else if (tipo == "duplo") {
            std::cout << "Mostrando obstáculo duplo na posição (" << x << ", " << y << ")." << std::endl;
            std::cout << "Mostrando obstáculo duplo na posição (" << x + largura_obstaculo + 10 << ", " << y << ")." << std::endl;
        } else if (tipo == "triplo") {
            std::cout << "Mostrando obstáculo triplo na posição (" << x << ", " << y << ")." << std::endl;
            std::cout << "Mostrando obstáculo triplo na posição (" << x + largura_obstaculo + 10 << ", " << y << ")." << std::endl;
            std::cout << "Mostrando obstáculo triplo na posição (" << x + 2 * (largura_obstaculo + 10) << ", " << y << ")." << std::endl;
        }
    }

    void mover() {
        y += velocidade;
    }

    bool fora_da_tela(int altura) {
        return y > altura;
    }

    bool colidir(int carro_x, int carro_y, int largura_carro, int altura_carro) {
        if (tipo == "normal") {
            return !(carro_x + largura_carro < x || carro_x > x + largura_obstaculo || carro_y > y + altura_obstaculo || carro_y + altura_carro < y);
        } else if (tipo == "duplo") {
            return !(carro_x + largura_carro < x || carro_x > x + 2 * largura_obstaculo + 10 || carro_y > y + altura_obstaculo || carro_y + altura_carro < y);
        } else if (tipo == "triplo") {
            return !(carro_x + largura_carro < x || carro_x > x + 3 * largura_obstaculo + 20 || carro_y > y + altura_obstaculo || carro_y + altura_carro < y);
        }
        return false;
    }

protected:
    int x, y;
    int largura_obstaculo, altura_obstaculo;
    std::string tipo;
    int velocidade;

private:
    std::string randomTipo(int nivel) {
        std::vector<std::string> tipos = {"normal", "duplo", "triplo", "lento", "quebra"};
        return tipos[rand() % tipos.size()]; // Seleciona um tipo aleatório
    }
};

class Lento : public Obstaculo {
public:
    Lento(int nivel, int largura, int altura_obstaculo, int largura_obstaculo, int velocidade)
        : Obstaculo(nivel, largura, altura_obstaculo, largura_obstaculo, velocidade) {
        tipo = "lento"; 
    }

    void mostrar() override {
        std::cout << "Mostrando obstáculo lento na posição (" << x << ", " << y << ")." << std::endl;
    }

    void efeito(int &velocidade_carro) {
        velocidade_carro = std::max(velocidade_carro - 10, 1);
    }
};

class ZeroCombustivel : public Obstaculo {
public:
    ZeroCombustivel(int nivel, int largura, int altura_obstaculo, int largura_obstaculo, int velocidade)
        : Obstaculo(nivel, largura, altura_obstaculo, largura_obstaculo, velocidade) {
        tipo = "quebra"; 
    }

    void mostrar() override {
        std::cout << "Mostrando quebra-mola na posição (" << x << ", " << y << ")." << std::endl;
    }

    void efeito(int &velocidade_carro) {
        velocidade_carro = 0; 
    }
};