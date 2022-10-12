#include <stdio.h>
int sum (int a,int b)
{
    return a+b;
}
int main()
{
    int d;
    printf("The sum of 5 and 10 is :%d\n",sum(5,10));  //teasting a function
    int (*ptr) (int ,int); // declaring a function pointer
    ptr=&sum;  // creating a function pointer
    d =(*ptr)(6,7); //Derefrecing a function pointer
    printf("The value of d is: %d\n",d);
    return 0;
}