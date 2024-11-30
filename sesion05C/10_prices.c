/*
Encontrar el precio más alto dentro de un array de 100 numeros y aplicar el 10% de descuento
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_PRICES 100

/*Definimos las futuras funciones*/
void imprime_precios(int precios[]);
int busca_pos_max(int precios[]);

/*Funciones*/

int main(){

    // Array de precios
    int precios[MAX_PRICES];
    int max_pos_price;

    srand(time(NULL));

    // Inicialización aleatoria de la variable precios
    for (int i=0; i<MAX_PRICES; i++){
        precios[i] = rand () % (1500-10+1) + 10;
    }

    imprime_precios(precios);

    // Busca el máximo
    max_pos_price=busca_pos_max(precios);
    //Imprime
    printf("El máximo precio es %d, aplicado el descuento es %.2f", precios[max_pos_price], (precios[max_pos_price]-precios[max_pos_price]*0.1));

}

void imprime_precios(int precios[]){
    for (int i = 0; i < MAX_PRICES; i++){
        printf("%d", precios[i]);
        if((i+1)%5!=0) printf(",");
        else printf("\n");
    }
}

int busca_pos_max(int precios[]){
    int max=0, pos_max=0;

    for (int i=0; i < MAX_PRICES; i++){
        if (precios[i]>max){
            max=precios[i];  /*Cambia el precio max si el siguiente supera al anterior*/
            pos_max=i; /*Gaurda la posición del precio max*/
        }
    }
    return pos_max;
}
