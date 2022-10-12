#include <stdio.h>
void func1(int array[])
{
    for (int i = 0; i < 4; i++)
    {
        printf("The value at %d array is %d\n ",i,*(array+i));  //arry[i]
    }
    array[0]=357;  //very important point that if you change any value here , it reflected in main
}

void func2(int *ptr)
{
    for (int i = 0; i < 4; i++)
    {
        printf("The value at %d array is %d\n ",i,*(ptr+i)); //ptr[i]
    }
    *(ptr+2)=10;
}

void func3(int arr[2][2])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("The value of %d ,%d is %d\n",i ,j ,arr[i][j]);
        }
        
    }
    
}
int main()
{
    // int arr[]={8,9,7,6};
    // printf("The value of 0 index is %d\n",arr[0]);
    // func1(arr);
    // printf("The value of 0 index is %d\n",arr+1);
    // func2(arr);
    // func2(arr);

    int arr[][2]={{3,8},{7,23}};
    func3(arr);
    return 0;
}