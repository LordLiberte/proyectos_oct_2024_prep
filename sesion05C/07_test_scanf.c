/*

* Ejemplo de scanf

*/

#include <stdio.h>

int main (void) {
    char cadena[80];  // array
    int entero1, entero2;
    float decimal;

    printf("Introduce dos enteros separados por un espacio: \n");
    scanf("%d %d", &entero1, &entero2);  // & es para la dirección de memoria que necesita scanf -> NECESARIO!! No se puede cambiar sin acceder a la memoria.

    printf("Introduce un numero decimal: \n");
    scanf("%f", &decimal);

    printf("Intoruce una cadena: \n");
    scanf("%s", cadena);  // Cadena es una dirección de memoria -> Cadena[0] es el valor de la primera posición, se puede usar &cadena[0]

    printf("Esto es todo lo que has escrito\n");
    printf("%d %d %f %s\n", entero1, entero2, decimal, cadena);
    return 0;

} 