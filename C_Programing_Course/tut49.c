#include <stdio.h>

int func1(int a, int b)
{
    return a + b;
}
int main()
{
    int sum;
    sum = func1(5,10);
    printf("%d-->\n" ,sum);

    return 0;
}