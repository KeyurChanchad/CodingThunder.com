#include <stdio.h>
int main()
{
    int a=16;
    int *ptr=&a;
    int *ptr2=NULL;
    printf("The value of a is %d\n",a);
    printf("The address of a is %x\n",&a);
     printf("The address of a by pointer is %x\n",ptr);
     printf("The address of some garbage is %p\n",ptr2);
    printf("The value of pointer variable is %d\n",*ptr);
    printf("The address of a pointer is %d\n",&ptr);
    return 0;
}