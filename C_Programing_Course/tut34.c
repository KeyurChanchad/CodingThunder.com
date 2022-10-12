#include <stdio.h>
void printstr(char string[])
{
    int  i=0;
    while (string[i]!='\0')
    {
        printf("%c",string[i]);
        i++;
    }
    printf("\n");
    
}
int main()
{
    // char str[]={'k','e','y','u','r','\0'};
    // char str[]={"Keyur"};
    char str[30];
    printf("Enter string:");
    gets(str);
    printf("Using puts:");
    puts(str);
    printf("Using printstr function:");
    printstr(str);
    printf("Using printf %s",str);
    return 0;
}   