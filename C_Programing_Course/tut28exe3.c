#include <stdio.h>

fibo_iterative(int num)
{
    int a, b;
    a = 0;
    b = 1;
    for (int i = 0; i < num - 1; i++)
    {
        b = a + b;
        a = b - a;
    }
        return a;
}

fibo_recursive(int n)
{
    if (n == 1 || n == 2)
    {
        return n - 1;
    }
    else
    {
        return fibo_recursive(n - 1) + fibo_recursive(n - 2);
    }
}

int main()
{
    int num;
    printf("Enter the number you want to print fibonacci series:\n");
    scanf("%d", &num);
    printf("The value of fibonacci number at position %d using recursion function is %d\n ", num, fibo_recursive(num));
    printf("The value of fibonacci number at position %d using  iterative function is %d\n", num, fibo_iterative(num));
    return 0;
}