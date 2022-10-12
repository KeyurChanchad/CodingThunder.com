#include<stdio.h>
void main()
{
    char ch;
    FILE *fp,*fp2;
    int i;
    fp=fopen("jalal.txt","r");
    fp2=fopen("reverse.txt","w");
    fseek(fp,-1,SEEK_END);
    i=ftell(fp);
    printf("current position is %d. \n",i);

 while(i>=0)
    {
        ch=getc(fp);
        printf("%c",ch);
        putc(ch,fp2);
        fseek(fp,-2,SEEK_CUR);
        i--;

    }
    fclose(fp);
    fclose(fp2);
}
