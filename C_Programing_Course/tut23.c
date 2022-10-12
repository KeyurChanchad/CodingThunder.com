#include <stdio.h>
int main()
{
    int marks[2][4]={{5,6,75,6},
                    {2,4,6,8}};
    // marks[0]=16;
    // printf("mark of student 1 is %d\n", marks[0]);
    // marks[0]=15;
    // marks[1]=20;
    // marks[2]=25;
    // marks[3]=30;
    //     printf("mark of student 1 is %d", marks[0]);

    // for (int i = 1; i<=4; i++)
    // {
    //     printf("Enter the value of %d of array:",i);
    //     scanf("%d", &marks[i]);
    // }

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 4; j++)
        {
        // printf("The value of %d, %d of array is %d:\n" ,i,j ,marks[i][j]);
        printf("%d ",marks[i][j]);
        }
        printf("\n");
        
    }
}
    