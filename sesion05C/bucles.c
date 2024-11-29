# include <stdio.h>

# define NUM_SUM 100  /*Define una constante*/

/*Variables*/
int main() {
    int suma = 0;  /*Definimos un integer*/
    int cont=0;

    for (int i = 0; i<NUM_SUM; i++)  /*Definimos un bucle, primero definimos eltipo de dato y su valor inicial, luego la condición que se comprueba y luego la acción a realizar*/
    {
        suma = suma + i;
    }

    printf("La suma total usando FOR es: %d\n", suma);
    suma=0;

    while (cont<NUM_SUM)
    {
        suma = suma + cont;
        cont++;
    }

    printf("La suma usando WHILE es: %d", suma);

}