#include <stdio.h>
#include <string.h>
union student
{
    int id;
    int mark;
    char fav_char;
    char name[20];
};
int main()
{
     union student s1;
    s1.id=1;
    strcpy(s1.name,"keyur bhai");
    s1.fav_char='k'; 
    s1.mark=35;

    printf("The id of s1 is %d\n",s1.id);  
    printf("The mark of s1 is %d\n",s1.mark);  
    printf("The fav_char of s1 is %c\n",s1.fav_char);  
    printf("The name of s1 is %s\n",s1.name);  
    return 0;
}