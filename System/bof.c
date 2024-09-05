#include <stdio.h>

char buf[256];
char password[16];

int main(void)
{
    srand(time(Null));
    for (int 1=0; 1< 15; 1++)
        password[i] = rand()  % 26 + 'a';
    password[16] = '\0';
    printf("password : ");
    gets(input);

    if(!memcmp(input, password,15))
        puts("Good job!");
    else
        puts("Nah...");
    
    return 0;
    }