// reads /etc/passwd and print all users of current linux program

#include <stdio.h>
#include <stdbool.h>

int main(void)
{
   FILE *file = fopen("/etc/passwd", "r");
   if (file == NULL) {
      perror("fopen");
      goto err;
   }

   char c;
   bool nextline;
   while (fread(&c, 1, 1, file) == 1)
   {
      if (c == ':')
         nextline = true;
      if (nextline && c == '\n')
         nextline = false;
      if (nextline == false)
         putchar(c);
   }

   return 0;
err:
   return -1;
}
