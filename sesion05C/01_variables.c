# include <stdio.h>

int main(){
    int a=10,b=34;  /*Definimos las variables y su tipo de dato*/

    if (a>b) {
        b--, a=a+5; 
        }  /* El () es la condicion a cumplir, los {} es las acciones a realizar {si es TRUE, si es FALSE}*/
    else {
        a++, b=b+5; 
        }
    if (b-a!=7) b=5;

}