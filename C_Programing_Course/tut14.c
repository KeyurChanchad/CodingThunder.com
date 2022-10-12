#include<stdio.h>
int main( )
{
    int num,i=0;
    printf("Enter your number:");
    scanf("%d",&num);
    while(i<num)
    {
        printf("%d\n",i+1);
        i=i+1;
    }
    return 0;
}