#include<stdio.h>
int main( )
{   int age,mark;
    printf("Enter your age:\n");
    scanf("%d",&age);
    printf("Enter your marks:\n");
    scanf("%d",&mark);

    switch(age)
    {
        case 3:
        printf("The age is 3.\n");
        
        switch(mark)
        {
            case 45:
            printf("Marks is 45.");
            break;

            default:
            printf("You are not pass");
        }
        break;

        case 10:
        printf("The age is 10.");
        break;

        case 18:
        printf("The age is 18.");
        break;

        default:
        printf("Age is not 3,10 or 18");
    }
    return 0;
}