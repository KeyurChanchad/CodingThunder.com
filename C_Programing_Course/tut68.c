#include<stdio.h>
int main(int argc, char const *argv[])
{
   printf("The value of argc is: %d\n",argc);
   for (int i = 0; i < argc; i++)
   {
       printf("This argument at index of %d and value is: %s\n",i,argv[i]);
   }
    // run program and write tut68.exe keyur chanchad
    return 0;
}
