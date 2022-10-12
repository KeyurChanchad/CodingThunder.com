#include <stdio.h>
int main()
{
    int num;
    float km, pound, cm, inches, second;
    while (1)
    {
        printf("Enter which type of conversion do you want? :\n 1.Kilometer to Miles\n 2.Pound to Kilometer\n 3.Centimeter to inches\n 4.Centimeter to meter\n 5.inches to foot\n 6.Exit\n ");
        scanf("%d", &num);

        switch (num)
        {

        case 1:
            printf("Enter number in km:");
            scanf("%f", &km);
            second = km * 0.621371;
            printf("%.2f km = %.2f miles\n\n", km, second);
            break;

        case 2:
            printf("Enter weight in pound:");
            scanf("%f", &pound);
            second = pound * 0.453592;
            printf("%.2f pound = %.2f kg\n\n", pound, second);
            break;

        case 3:
            printf("Enter the cm:");
            scanf("%f", cm);
            second = cm * 0.393701;
            printf("%.2f cm = %.2f inches\n\n", cm, second);
            break;

        case 4:
            printf("Enter the cm:");
            scanf("%f", &cm);
            second = cm * 0.01;
            printf("%.2f cm = %.2f meter\n\n", cm, second);
            break;

        case 5:
            printf("Enter the inches:");
            scanf("%f", &inches);
            second = inches * 0.0833333;
            printf("%.2f inches = %.2f feet\n\n", inches, second);
            break;

        case 6:
              goto end;

        default:
            printf("You have entered invalid number:");
        }
    }
   end:
   return 0; 
}
