/*APLICACIÓN PARA CONVERTIR UNIDADES CELSIUS A FAHRENHEIT*/

#include <stdio.h>
# include <stdlib.h>
# include <time.h> /*Librería necesariara para srand*/

int main(){

    /*Definimos variables a usar y su tipo de dato*/
    float cel, fahr;  /*Definimos punto flotante*/
    int min, max, paso;   /*Definimos enteros*/

    
    int num_temperaturas;
    srand(time(NULL));  /*Necesario para rand ()*/
    int temperatura;

    /*Inicialización de variables necesarias*/
    min = 0;
    max = 300;
    paso=20;

    fahr=min;
    cel=min;

    /*Bucle while*/

    while (fahr<=max){

        cel=5*(fahr-32)/9;
        printf("Conversion temperatura ºF: %.2f ºC: %.2f\n", fahr, cel);
        fahr = fahr + paso;
    }

    while (num_temperaturas <= 24) {

        //Numero aleatorio entre 0 y 100
        temperatura = rand () % 15;
        printf("Temperatura %d", temperatura);
        if(temperatura>=10){
            printf("La cámara se descongela");
            break;
        }

    num_temperaturas++;

    }
}