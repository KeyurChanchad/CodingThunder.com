#include<stdio.h>
void main()
{
    char ch;
    FILE *fp,*fp2;
    int i,logic=0;
    fp=fopen("jalal.txt","r");
    fp2=fopen("realspace.txt","w");
    while((ch=getc(fp))!=EOF)
    {
        if(ch==' ')
        {
            if(logic==0)
            {
                printf("%c",ch);
                putc(ch,fp2);
                logic=1;
            }
        }
        else
        {
            printf("%c",ch);
            putc(ch,fp2);
            logic=0;
        }
    }
    fclose(fp);
    fclose(fp2);

}
