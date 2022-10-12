#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a=31;
    int *ptr; // This is wild pointer.
    // *ptr=31; This is not  a good thing to do 
    ptr= &a;
    printf("The value of a is %d\n",*ptr);

}