#include<stdio.h>
int main( )
{
    int i,age;
    for(i=0;i<10;i++)
    {
        printf("No:%d\t Enter your age:\n",i);
        scanf("%d",&age);

        // if(age<10)
        // {
        //     break;
        // }

        if(age>10)
        {
            continue;
        }
        printf("This not skipped:\n");
        printf("This not skipped:\n");
        printf("This not skipped:\n");
        printf("Keyur is good boy:\n");
    }
    return 0;
}