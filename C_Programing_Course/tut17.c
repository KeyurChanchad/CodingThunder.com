#include<stdio.h>
int main( )
{
    int i,j,num;
    printf("Hello Keyurbhai\n");
    for(i=0;i<5;i++)
    {
        printf("%d \t",i);
        for(j=0;j<10;j++)
        {
        printf("Enter the number, enter 0 to exit\n");
        scanf("%d",&num);
        if(num==0)
        {
            goto end;
        }
        }

    }
    end:
    return 0;
}