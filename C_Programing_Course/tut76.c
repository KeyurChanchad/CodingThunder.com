#include <stdio.h>
#include <math.h>
float edistance(int x1, int x2, int y1, int y2)
{
    int a;
    a = (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2);
     return sqrt(a);
}
float areaofcircle(int x1,int y1,int x2,int y2, float(*edistance)(int x1, int x2, int y1, int y2))
{
    return x1,y1,x2,y2;
}
int main()
{
    int x1,x2,y1,y2;
    float dist;
    printf("Enter value of X1:\n");
    scanf("%d",&x1);
    printf("Enter value of Y1:\n");
    scanf("%d",&y1);
    printf("Enter value of X2:\n");
    scanf("%d",&x2);
    printf("Enter value of Y2:\n");
    scanf("%d",&y2);

    dist= areaofcircle(x1,y1,x2,y2,(edistance));
    printf("The Distance is %2.f\n",dist);
    return 0;
}