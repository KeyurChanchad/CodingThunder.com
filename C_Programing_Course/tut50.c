#include <stdio.h>
#include <stdlib.h>
int main()
{
        char *ptr;
        int i=0,n;
   while (i<3)
   {
        printf("Employee %d: Enter number of character in ID:\n",i+1);
        scanf("%d", &n);
        ptr = (char *) malloc ((n+1) * sizeof(char));
        printf("Enter %d employee ID:\n", i + 1);
        scanf("%s",ptr);
       printf("Employee %d ID: %s\n",i+1 ,ptr);
       free(ptr);
       i++;
   }
}