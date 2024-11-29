/*
* Muetsra al usuario un menú
*/

# include <stdio.h>

int get_menu_choice(void);  // Necesario declarar funciones de forma explicita -> si se quita -> error: implicit declaration of function 'get_menu_choice' [-Wimplicit-function-declaration]

void main(void){
    int choice;

    choice = get_menu_choice();
    printf("You have chosen menu #%d\n", choice);
    printf("\n");

}

int get_menu_choice(void){
    int selection = 0;

    do
    {
        printf("1 - Add a Record");
        printf("\n2 - Change a record");
        printf("\n3 - Delete a record");
        printf("\n4 - Quit");
        printf("\nEnter  selection: ");
        /* scanf("%d", &selection); */

        scanf("%d", &selection, 1);

    } while ((selection < 1) || (selection > 4));

    return selection;
    
}