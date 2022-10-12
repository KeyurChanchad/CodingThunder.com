#include<iostream>
using namespace std;
int glob=85;
int sum()
    {
        cout<<"\nthis is globle variable :"<<glob;
    }

int main()
{
int a=5,b=9, glob=15;
 glob=96;
char c='K';
float pi=3.14;
double dbl=85.79;
bool truee=true;
bool falsee= false;

cout<<"Here value of a is :"<<a <<"\nValue of b is :"<<b;
cout<<"\nThe character of c is :"<<c;
cout<<"\nThe value of pi is :"<<pi ; //<<sizeof(pi);
cout<<"\nthe value of double :"<<dbl ;//<<sizeof(dbl);
sum();
cout<<"\nThis print local :"<<glob
    <<"\nThis is boolean true :"<<truee 
    <<"\nThis is boolean flase :"<<falsee;

return 0;
}