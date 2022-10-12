#include<stdio.h>
int length(char *);
void main()
{
    char name[20];
    int l;
    printf("\nEnter your name:");
    scanf("%s",name);
    l=length(name);
    printf("\nLength is : %d",l);
}
int length (char *p)
{
    int i=0;
    while(*p!='\0')
    {
        p++;
        i++;
    }
    return i;
}
