#include<stdio.h>
void upper(char *);
void main()
{
    char name[10];
    printf("\nEnter your name:");
    scanf("%s",name);
    upper(name);
    printf("\nUppercase is : %s",name);

}
void upper(char *i)
{
    while(*i!='\0')
    {
        if(*i>=97 && *i<=122)
            *i=*i-32;
    }
    *i++;
}
