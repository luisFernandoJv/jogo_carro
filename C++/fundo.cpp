#include <iostream>

class Fundo {
public:
    Fundo(int largura, int altura) : largura(largura), altura(altura) {}

    void desenhar() {

        std::cout << "Desenhando o fundo..." << std::endl;
    }

private:
    int largura;
    int altura;
};
