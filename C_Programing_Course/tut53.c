#include <stdio.h>
int main()
{
    int k = 16;
    int *ptr = NULL;
    if (ptr != NULL)
    {
        printf("The value of a is %d",* ptr);
    }
    else
    {
        printf("The pointer is NULL pointer can not be derefrence\n");
    }

    return 0;
}