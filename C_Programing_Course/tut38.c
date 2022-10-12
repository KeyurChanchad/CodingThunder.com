#include <stdio.h>
// typedef <privious name> <alis name/new>

typedef struct student 
{
    int id;
    int mark;
    char fav_char;
    char name[20];
}std;
int main()
{
    // int *a,b;
    typedef int* intptr;
    intptr a,b;
    int c=96;
    a=&c;
    b=&c;

    // typedef unsigned long ul;
    // ul li1,li2,li3;
    // typedef int integer;
    // integer a=30;
    // printf("The value of a is %d",a);


    // struct student s1;
    // std s1;

    // s1.id=1;
    // s1.mark=35;
    // s1.fav_char='g';

    // printf("The value Id of s1 is %d\n",s1.id);
    // printf("The value mark of s1 is %d",s1.mark);
    // return 0;
}