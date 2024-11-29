/*APLICACIÓN PARA CONVERTIR UNIDADES CELSIUS A FAHRENHEIT*/

#include <stdio.h>

int main(){

    /*Definimos variables a usar y su tipo de dato*/
    float cel, fahr;  /*Definimos punto flotante*/
    int min, max, paso;   /*Definimos enteros*/

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
}