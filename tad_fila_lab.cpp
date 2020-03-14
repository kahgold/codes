/*Exercício de hoje: TAD FILA

Implementar um algoritmo para testar um TAD FILA com as seguintes 
opções de menu:
- 0 -> encerrar
- 1 -> inserir na fila (enqueue)
- 2 -> extrair da fila (dequeue)
- 3 -> localizar um elemento (informa o valor e retorna a posição
na fila)
- 4 -> quantidade de elementos na fila
- 5 -> imprimir a fila*/

#include "tad_fila_lab.h"
#include "tad_fila_main_lab.cpp"
#include <iostream>

using namespace std;

class TadFila{
    private:
        int numeros[10];
        int inicio, fim, qtd;

    public:
        TadFila();
        bool inserir(int n);
        int extrair();
        int localizar(int n);
        int quantidade();
        void imprimir();
};

bool TadFila::vazia(){
    if(qtd == 0){
        return true;
    }

    else{
        return false;
    } 
}

bool TadFila::cheia(){
    if(qtd == fim){
        return true;
    }

    else{
        return false;
    }  
}

bool TadFila::inserir(int n){
    if(cheia() == true){
        return false;
    }

    if(fim == qtd - 1){
        fim = 0;
    }

    else{
        fim++;
    }

    numeros[fim] = n;
    qtd++;
    return true;
}

int TadFila::extrair(){
    if(vazia() == true)
        return false;
    
    if(inicio == qtd)
        inicio = 0;
    
    else{
        inicio++;
    }

    qtd--;
    return true;
}

int TadFila::localizar(int n){
    
}

int TadFila::quantidade(){
    return qtd;
}

void TadFila::imprimir(){
    for(int i = 0; i < 10; i++){
        cout << numeros[i] << ' ';
    }
}