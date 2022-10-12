#include <stdio.h>
#include<stdlib.h>
int palindrom(int num)  // return 1 :palindrom and return 0 :not palindrom
{
    int reverse=0 ;
    int original= num;
    // Let reverse the number
    while (num!=0)
    {
        reverse = reverse * 10 + num % 10;
        num= num / 10;
    }
    printf("This is revere number:%d\n",reverse);

    if (original==reverse)
    {
        return 1;
    }
    else
    {
    return 0;      
    }
    
}
int main()
{
    int number;
    printf("Enter the number to check whether it palindrom or not:\n");
    scanf("%d",&number);
    getchar();
    if (palindrom(number))
    {
        printf("This is palindrom number\n");
    }
    else
    {
        printf("This is not palindrom\n");
    }
    
    
    return 0;
}