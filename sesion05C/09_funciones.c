#include <stdio.h>

/*EJEMPLO*/
/*

[tipo] [nombre](){

    cuerpo de la función

}

*/


/* RETURN -> PERMITE SALIR DE LA FUNCIÓN CUANDO SE INVOCA Y DEVOLVER UN VALOR SI ES NECESARIO*/
/* Si la función es tipo void no se pueden devolver valores */
int Comparacion(int a, int b){
    if (a>b) return 1;  /*a es mayor que b*/
    if (b>a) return -1;  /*b es mayor que a*/
    return 0; /*a y b son iguales*/
 }