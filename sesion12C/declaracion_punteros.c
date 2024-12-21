#include <stdio.h>

int *puntero;

int main(){
    int  a=10;  // variable integer
    puntero = &a;  // asigna la direccion de la variable
    printf("El valor de a es: %d\n", a);
    printf("La dirección de a es: %p\n", puntero);

    return 0; // Sirve para indicar que el programa terminó correctamente
}