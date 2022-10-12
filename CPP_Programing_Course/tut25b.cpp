#include<iostream>
using namespace std;
 class complex 
 {
     int a,b;  // By defualt it is private:
    
     public:
     void setdata(int v1,int v2)
     {
         a=v1;
         b=v2;
     }
     void SetDataBySum(complex o1,complex o2)    //Object is passed in function by Argument
     {
         a = o1.a + o2.a;
         b = o1.b + o2.b;
     }

     void printcomplex()
     {
            cout<<"The complex number is "<<a<<" + "<<b<<"i"<<endl;
     }
 };
int main()
{
    complex c1,c2,c3;
    c1.setdata(1,2);
    c1.printcomplex();

    c2.setdata(3,4);
    c2.printcomplex();

    c3.SetDataBySum(c1,c2);
    c3.printcomplex();

return 0;
}