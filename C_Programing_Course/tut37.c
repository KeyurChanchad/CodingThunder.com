#include <stdio.h>
#include <string.h>
struct student
{
    int id;
    int mark;
    char fav_char;
    char name[20];
};
struct student keyur,mahesh;
    
void print(){
    printf("%s",keyur.name);
}

int main()
{
    // struct student keyur,mahesh;
    keyur.id=1;
    mahesh.id=2;
    keyur.mark=46;
    mahesh.mark=20;
    keyur.fav_char='k';
    mahesh.fav_char='m';

    printf("Keyur id is %d\n",keyur.id);
    printf("mahesh id is %d\n",mahesh.id);

    printf("Keyur mark is %d\n",keyur.mark);
    printf("mahesh mark is %d\n",mahesh.mark);

    printf("Keyur fav_char is %c\n",keyur.fav_char);
    printf("mahesh fav_char is %c\n",mahesh.fav_char);

    strcpy(keyur.name, "keyur is a good boy");
    strcpy(mahesh.name, "mahesh is a good boy");
    // printf("%s\n",keyur.name);
    printf("%s\n",mahesh.name);

    print();
    return 0;
}