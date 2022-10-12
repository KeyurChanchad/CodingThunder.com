#include<stdio.h>
int main( )
{
    int age;
    printf("Enter your age:\n");
    scanf("%d",&age);

    printf("You have enter %d as age:\n ",age);
    if(age>=18)
    {
        printf("you can vote!");
    }
    else if(age>=10)
    {
        printf("you can vote between 10 to 18 for kids!");
    }
    else if(age>=3)
    {
        printf("you can vote between 3 to 10 for babies!");
    }
    else{
        printf("you can not vote!");
    }
    return 0;
}