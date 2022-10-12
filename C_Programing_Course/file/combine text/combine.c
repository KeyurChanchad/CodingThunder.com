#include<stdio.h>
void main()
{
    FILE *fp,*fp2,*fp3;
    char ch;
    fp=fopen("keyur.txt","r");
    fp2=fopen("chanchad.txt","r");
    fp3=fopen("combine.txt","w");
    while((ch=getc(fp))!=EOF)
    {
        putc(ch,fp3);
    }
    while((ch=getc(fp2))!=EOF)
    {
        putc(ch,fp3);
    }
  fclose(fp);
  fclose(fp2);
  fclose(fp3);

}
