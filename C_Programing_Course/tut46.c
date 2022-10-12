#include <stdio.h>
 typedef struct driver
{
    char name[10];
    char lno[10];
    char route[10];
    int kms;
}dr;

int main()
{
    dr dr1,dr2,dr3;
    printf("Enter three driver's details:\n\n");

    printf("Enter first driver details:\n");
        printf("Enter name of driver:\n");
        scanf("%s",&dr1.name);

        printf("Enter licence of driver:\n");
        scanf("%s",&dr1.lno);

        printf("Enter route of driver:\n");
        scanf("%s",&dr1.route);

        printf("Enter number of Kms dirve:\n");
        scanf("%d",&dr1.kms);

    printf("Enter second driver details:\n");
        printf("Enter name of driver:\n");
        scanf("%s",&dr2.name);

        printf("Enter licence of driver:\n");
        scanf("%s",&dr2.lno);

        printf("Enter route of driver:\n");
        scanf("%s",&dr2.route);

        printf("Enter Kms of driver:\n");
        scanf("%d",&dr2.kms);

    printf("Enter third driver details:\n");
        printf("Enter name of driver:\n");
        scanf("%s",&dr3.name);

        printf("Enter licence of driver:\n");
        scanf("%s",&dr3.lno);

        printf("Enter route of driver:\n");
        scanf("%s",&dr3.route);

        printf("Enter Kms of driver:\n");
        scanf("%d",&dr3.kms);


        printf("First driver details:\n Name:%s\n",dr1.name);
        printf("Licence NO:%s\n",dr1.lno);
        printf("Route:%s\n",dr1.route);
        printf("Kms:%d\n",dr1.kms);

        printf("Second driver details:\n Name:%s\n",dr2.name);
        printf("Licence NO:%s\n",dr2.lno);
        printf("Route:%s\n",dr2.route);
        printf("Kms:%d\n",dr2.kms);

        printf("Third driver details:\n Name:%s\n",dr3.name);
        printf("Licence NO:%s\n",dr3.lno);
        printf("Route:%s\n",dr3.route);
        printf("Kms:%d\n",dr3.kms);

       
    return 0;
}