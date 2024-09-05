#include <stdio.h>

int sum(int a, int b, int c) {
    return a + b + c;
}

int main(void)
{
   int a, b, c;
   scanf("%d %d %d", &a, &b, &c);
   
   int s = sum(a, b, c);
   printf("%d", s);

   return 0;
}
