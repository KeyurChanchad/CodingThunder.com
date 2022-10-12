#include <stdio.h>
#include <stdlib.h>
int sum=10;
int functiondangling()
{
    int a,b,sum2;
     a=3;
     b=5;
    sum=a+b;
    return &sum;
}
int main2()
{
    // case 1: De allocation of memory block
    int *ptr =(int *) malloc (5*sizeof(int));
    ptr[0]=25;
    ptr[1]=35;
    ptr[2]=45;
    ptr[3]=55;
    free(ptr);// ptr is a dangaling pointer.

    // case 2: Function returing local variable address:
    int *dangptr = functiondangling();  // dangptr is now a dangling pointer

    // case 3: if a variable goes out of scope:
    int *danglingptr;
    {
        int a=12;
        danglingptr = &a;
    }
    // Here variable a goes out of scope which means danglingptr is pointing to a location which is free and hence danglingptr is now  a dangling. 
    return 0;
}