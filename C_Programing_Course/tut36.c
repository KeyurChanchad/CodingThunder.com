#include <stdio.h>
void  revarr(int array[])
{
  int tmp;
  for (int i = 0; i < 7/2; i++)
  {
  tmp=array[i];
  array[i]=array[6-i];
  array[6-i]=tmp; 
  }
  
}
void printarr(int arr[])
{
  for (int i = 0; i < 7; i++)
  {
    printf(" %d,",arr[i]);
  }
  
}
int main()
{
    int arr[]={1,2,3,4,5,6,7};
    printf("Before reverse array:\n");
    printarr(arr);
    printf("\nAfter reverse array:\n");
    revarr(arr);
    printarr(arr);
    return 0;
}