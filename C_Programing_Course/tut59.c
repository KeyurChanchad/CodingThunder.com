# include <stdio.h>
# include "tut54.c"
# define PI 3.14  // This is declare variable
#define square(r) r*r // this is macros  
int main()
{
    float var = PI;
    int redius=4;
    int *ptr= functiondangling();
    printf("The value of PI is %f\n",var);
    printf("The area of circle is %f\n",PI * square(redius));
    return 0;
}