#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int genrate(int n)
{
    srand(time(NULL)); // this is a function of generate a random number
return rand()%n;
}
int main()
{
    printf("The random number between 0 to 50 :%d\n",genrate(50));
    return 0;
}