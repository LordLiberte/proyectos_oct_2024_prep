/*
* Programa de temperaturas
*/

# include <stdio.h>
# include <stdlib.h>
# include <time.h> /*Librería necesariara para srand*/


void main() {

    int numero;

    //Obtener un numero aleatorio entre M y N
    srand(time(NULL));
    numero = rand () % 46;

    printf("El numero obtenido es: %d\n", numero);

    if (0 <= numero && numero <= 10)
    {
        printf("Hace mucho frio");
    }

    else if (10 < numero && numero <= 20)
    {
        printf("Hace fresquito");
    }

    else if (20 < numero && numero <= 30)
    {
        printf("No se está mal");
    }
    
    else if (30 < numero && numero <= 40)
    {
        printf("Comienza a hacer calor");
    }

    else {
        printf("Muero achicharrado");
    }

}