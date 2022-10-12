#include<stdio.h>
void main()
{
    char ch;
    FILE *fp;
    int i=0;
    fp=fopen("2.txt","r");
    while((ch=getc(fp))!=EOF)
    {
        i++;
    }
    printf("The size of this file is %d Byte.",i+1);

}
