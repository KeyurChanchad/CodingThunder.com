#include<stdio.h>
void swap(int *,int *);
void main()
{
    int x,y;
    printf("\n Enter first number:");
    scanf("%d",&x);
    printf("\n Enter second number:");
    scanf("%d",&y);
    swap(&x,&y);
    printf("\n First number is =%d",x);
    printf("\n second number is =%d",y);
}
void swap(int *p,int *q)
{
    int tmp;
    tmp=*p;
    *p=*q;
    *q=tmp;
}
