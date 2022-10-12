#include <stdio.h>

void starpattern(int rows)
{
    int i, j;
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j <= i; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
}

void revstarpattern(int rows)
{
    int i, j;
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < rows - i; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
}

void mountain(int rows)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < rows - i + 1; j++)
        {
            printf(" ");
        }
        for (int k = 0; k <= i; k++)
        {
            printf("* ", k);
        }
        printf("\n");
    }
}

int main()
{
    int rows, type;
    printf("Enter 1. star pattern \n2. for reverse star pattern:\n3.mountain pattern");
    scanf("%d", &type);
    printf("\nHow many rows do you want to print:\n");
    scanf("%d", &rows);
    switch (type)
    {
    case 1:
        starpattern(rows);
        break;

    case 2:
        revstarpattern(rows);
        break;
    case 3:
        mountain(rows);
        break;

    default:
        printf("You have entered an invalid number:");
        break;
    }
}