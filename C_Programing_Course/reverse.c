#include<stdio.h>
void reverse(char *);
void main()
{
    char name[10];
    printf("\nEnter name:");
    scanf("%s",name);
    reverse(name);
    printf("\nReverse is: %s",name);
}

void reverse(char *s)
{
    char *d,tmp ;
    d=s;
    while(*d!='\0')
    {
        d++;
        d--;
    }

    while(d>s)
    {
        tmp=*s;
        *s=*d;
        *d=tmp;
        s++;
        d--;
    }
}
