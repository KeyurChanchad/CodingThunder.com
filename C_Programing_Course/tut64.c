#include <stdio.h>
int main()
{
    FILE *ptr=NULL;
    // char string[30];
    //  *********Reding file***********
    // ptr=fopen("mytxt.txt","r");
    // fscanf(ptr,"%s",string);
    // printf("The content of file is %s:\n",string);

    // **********writting file*************
    char str[20]="keyur chanchad";
    ptr=fopen("mytxt.txt","w"); // append mode is writting+reading ="a"
    fprintf(ptr,"%s",str);
    printf("The content of file is %s:\n",str);
    fclose(ptr);
    return 0;
}