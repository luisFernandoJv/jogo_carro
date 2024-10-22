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

    Obstaculo obstaculo(1, 400, 50, 50, 5);
    obstaculo.mostrar();
    obstaculo.mover();

    return 0;
}