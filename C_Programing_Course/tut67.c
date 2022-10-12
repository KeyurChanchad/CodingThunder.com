#include <stdio.h>
int main()
{
    FILE *ptr=NULL;
    FILE *ptr2=NULL;
    // ptr = fopen("mytxt.txt","r");
//    char *c= fgetc(ptr);
//    printf("The character 1 of file is %c\n",c);
//     c= fgetc(ptr);
//    printf("The character 2 of file is %c\n",c);

    char str[30]="eyur";
    // fgets(str,5,ptr);
    // printf("The string is: %s\n",str);

    ptr = fopen("mytxt.txt","w");
fputc('K',ptr);
fputs(str,ptr);
    fclose(ptr);
    fclose(ptr2);
    return 0;
}