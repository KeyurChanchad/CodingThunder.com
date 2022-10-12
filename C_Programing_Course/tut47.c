#include <stdio.h>
#include <stdlib.h> // malloc,calloc,realloc,free

int main()
{
    //Use of malloc
    // int *ptr;
    // int n;
    // printf("Enter the size of the array you want to creat:");
    // scanf("%d",&n);
    // ptr=(int *) malloc (n * sizeof(int));

    // for  (int i = 0; i < n; i++)
    // {
    //     printf("Enter the value of %d of this array:\n",i+1);
    //     scanf("%d",&ptr[i]);
    // }

    // for (int i = 0; i < n; i++)
    // {
    //     printf("Enter the value of %d of this array is %d:\n",i,ptr[i]);
    // }


    //Use of calloc
    int *ptr;
    int n;
    printf("Enter the size of the array you want to creat:");
    scanf("%d",&n);
    ptr=(int *) calloc (n, sizeof(int));

    for  (int i = 0; i < n; i++)
    {
        printf("Enter the value of %d of this array:\n",i+1);
        scanf("%d",&ptr[i]);
    }

    for (int i = 0; i < n; i++)
    {
        printf("Enter the value of %d of this array is %d:\n",i,ptr[i]);
    }

    //Use of realloc
    printf("Enter the size of the new array you want to creat:");
    scanf("%d",&n);
    ptr=(int *) realloc (ptr, n*sizeof(int));

    for  (int i = 0; i < n; i++)
    {
        printf("Enter the value no %d of this array:\n",i);
        scanf("%d",&ptr[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("Enter the value no %d of this array is %d:\n",i,ptr[i]);
    }
    free(ptr);
}