#include<stdio.h>
#define pi 3.14
/* this is a multiline comments 

 and this is ignore by compilar */
int main( )
{
    int a;
//    const float pi=3.14;
// this connot work since pi is constant 
    a=10;
    // pi=5.14;
    printf("Hello World\n");
    printf("This is pi %15.2f\n",pi);
    printf("This is number %-15.2d \n",a);
    printf("Tab character is \t\t my backslash \\  and listen \a");
    
    return 0;
}

