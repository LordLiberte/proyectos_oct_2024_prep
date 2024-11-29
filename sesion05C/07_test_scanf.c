/*

* Ejemplo de scanf

*/

#include <stdio.h>

int main (void) {
    char cadena[80];
    int entero1, entero2;
    float decimal;

    printf("Introduce dos enteros separados por un espacio: \n");
    scanf("%d %d", &entero1, &entero2);  // & es para que el usuario meta valores

    printf("Introduce un numero decimal: \n");
    scanf("%f", &decimal);

    printf("Intoruce una cadena: \n");
    scanf("%s", cadena);

    printf("Esto es todo lo que has escrito\n");
    printf("%d %d %f %s\n", entero1, entero2, decimal, cadena);
    return 0;

} 