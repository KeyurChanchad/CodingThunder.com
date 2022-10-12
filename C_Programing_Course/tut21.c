#include <stdio.h>
fact(int num)
{
    if (num == 0 || num == 1)
    {
        return 1;
    }
    else
    {
       return( num * fact(num-1));
    }
}
int main()
{
    int num;
    printf("Enter the number:\n");
    scanf("%d", &num);
    printf("The factoraial %d is %d",num, fact(num));
    return 0;
}
