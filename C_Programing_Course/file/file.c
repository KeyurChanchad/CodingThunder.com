#include<stdio.h>
void main()
{
    FILE *fp,fp1;
    char ch;
    int i,logic=0;
    fp=fopen("2.txt","r");
    fp1=fopen("JALAL (2).txt","w");
    while((ch==getc(fp))!=EOF)
    {
        if(ch=' ')
        {
            if(logic==0)
            {
                printf("%c",ch);
                putc(ch,fp1);
                logic=1;
            }
        }
        else
        {
            printf("%c",ch);
            putc(ch,fp1);
            logic=0;
        }
    }
    fclose(fp);
    fclose(fp1);
}
