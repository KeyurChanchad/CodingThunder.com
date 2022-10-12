#include<stdio.h>
int main()
{
    int num,i;
    printf("Enter a number you want to make maltiplication table:");
    scanf("%d",&num);
    for(i=1;i<=10;i++)
    {
        printf("%d X %d= %d\n",i,num,i*num);
    }
    return 0;
}
