#include <iostream>
#include <cstdlib>
#include <ctime>
#include "fundo.cpp"
#include "carro.cpp"
#include "obstaculo.cpp"

int main() {
    std::srand(std::time(0));

    Fundo fundo(400, 600);
    fundo.desenhar();

    Carro carro(400, 600, 50, 100, 5);
    carro.mostrar();
    carro.mover();

    // Criando um obstáculo normal
    Obstaculo obstaculo(1, 400, 50, 50, 5);
    obstaculo.mostrar();
    obstaculo.mover();

    // Criando um obstáculo lento
    Lento obstaculo_lento(2, 400, 50, 50, 5);
    obstaculo_lento.mostrar();
    obstaculo_lento.mover();

    // Criando um quebra-mola
    ZeroCombustivel quebra_mola(2, 400, 50, 50, 5);
    quebra_mola.mostrar();
    quebra_mola.mover();

    // Aplicando os efeitos
    // obstaculo_lento.efeito(carro);
    // quebra_mola.efeito(carro);

    return 0;
}
