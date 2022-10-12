#include <stdio.h>
void changeval(int *add)
{
   *add=50;
}

int sum_sub(int *x, int *y)
{
    int tmp;
    tmp=*x;
    *x= *x+*y;
    *y =tmp-*y;
}
int main()
{
    int a=18, b=2;
    printf("The value of a is %d\n",a);
    printf("The value of b is %d\n",b);
    sum_sub(&a, &b);
    printf("The value of a is sum %d\n",a);
    printf("The value of b is subtraction %d\n",b);

    changeval(&a); // call by refreance
    printf("The value of a is %d\n",a);
    return 0;
}