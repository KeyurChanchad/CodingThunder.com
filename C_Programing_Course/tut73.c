#include <stdio.h>
int sum(int a,int b)
{
    return a+b;
}
void greetgmexecute(int (*fptr)(int,int))
{
    printf("Good morning\n");
    printf("The sum of 5 and 7 is :%d\n",fptr(5,7));
}
void greethello(int (*fptr)(int,int))
{  
    printf("Hello word \n");
    printf("The sum of 5 and 7 is :%d\n",fptr(5,7));
}
float avrg(float x,float y)
{
    return x+y/2 ;
}
void greetGEexecute(float (*ptr)(float,float))
{
    printf("Good Evenig\n");
    printf("The average of 5.5 and 7.5 is :%2.f\n",ptr(5.5,7.5));
}
int main()
{
    int (*fptr) (int,int );  //Return type (Function pointer) (Argument of data type)
    fptr=sum;               // fptr=&sum
    greetgmexecute(fptr);
    greethello(fptr);

    float (*ptr) (float ,float);
    ptr=&avrg;
    greetGEexecute(ptr);
    return 0;
}