#include <stdio.h>
int main()
{
    int a=34;
    int *ptra=&a;
    printf("%d\n", ptra);
    ptra++;
    printf("%d\n", ptra); //it + size of (char/int) for arcitacture
    printf("%d\n", ptra-2);

    int arr[]={2,4,5,7,3,1,9};
    // int *arrptra=arr;
    printf("value of array at position %d\n",arr[3]);
    printf("The address of first element %d\n",&arr[0]); 
    printf("The address of first element %d\n",arr); 
    printf("The address of second element %d\n",&arr[1]); 
    printf("The address of second element %d\n",arr+1); 
    // arr++  this line show arror 
    // arrptra--;
    printf("The value at address of first element %d\n",*(&arr[0])); 
    printf("The value at address of first element %d\n",*(arr)); 
    printf("The value at address of first element %d\n",arr[0]); 

    printf("The value at address of second element %d\n",*(&arr[1])); 
    printf("The value at address of second element %d\n",*(arr+1)); 
    printf("The value at address of second element %d\n", (arr[1])); 
    return 0;
}