#include <stdio.h>

int *puntero;
int *ptr1;
int *ptr2;

int main(){
    int  a=10;  // variable integer
    puntero = &a;  // asigna la direccion de la variable
    printf("El valor de a es: %d\n", a);
    printf("La dirección de a es: %p\n", puntero);

    int mi_array[] = {1, 2, 3, 4, 5};  // Un array debe llevar []
    ptr1 = &mi_array[0]; // Ahora el ptr apunta al primer entero de nuestro array
    ptr2 = &mi_array[1]; // Ahora el ptr apunta al segundo entero de nuestro array

    printf("El valor de mi_array[0] es: %d\n", ptr1);
    printf("El valor de mi_array[1] es: %d\n", ptr2);
    return 0; // Sirve para indicar que el programa terminó correctamente
}