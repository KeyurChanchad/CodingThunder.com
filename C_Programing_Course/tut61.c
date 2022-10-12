#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[2][3], b[3][2], result[2][2];
    int i, j, k, sum = 0;
    printf("Enter first Matrix:\n");
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 3; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    printf("Enter second Matrix:\n");

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 2; j++)
        {
            scanf("%d", &b[i][j]);
        }
    }
    //print the first matrix
    printf("The first matrix :\n");
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("[%d] ", a[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    printf("The second matrix:\n");
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 2; j++)
        {
            printf("[%d] ", b[i][j]);
        }
        printf("\n");
    }
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            for (k = 0; k < 3; k++)
            {
                sum += a[i][k] * b[k][j];
            }
            result[i][j] = sum;
            sum = 0;
        }
    }
    //print the resulted matrix
    printf("The result matrix:\n");
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 2; j++)
        {
            printf("[%d]", result[i][j]);
        }
        printf("\n");
    }
    return 0;
}