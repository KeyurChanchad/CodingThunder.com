#include<stdio.h>
int sum(int x,int y);

// with argument no return
void printstar(int n)
{
    int i;
    for(i=0;i<n;i++)
    printf("%c",'*');
}

int takenumber ()
{
    int num;
    printf("\nEnter number:");
    scanf("%d",&num);
    return num;
}

int main( )
{
    int a,b,c,d;
    a=10;
    b=15;
    c=sum(a,b);
    printf("The sum is %d:\n",c);

    printstar(10);

    d=takenumber();
    printf("\nThe takenumber is %d",d);
    return 0;
}
// with argument with return 
int sum(int x,int y)
{
    return(x+y);
}
