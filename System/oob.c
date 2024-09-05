#include <stdio.h>
#include <stdlib.h>

int array[16];
int password;

int main(int argc, char **argv, char **envp) {
    
    srand(time(NULL));
    for (int i = 0; i < 16; i++) {
        array[i] = rand();
    }
    paassword = rand();

    int index;
    printf("index: ");
    scanf("%d", &index);

    printf("= %d\n", array[index]);

    int input;
    printf("password: ");
    scanf("%d", &input);

    if (input == password) {
        puts("Good Job!");
    }
    else:
        puts("Nah..");

    return 0;
}