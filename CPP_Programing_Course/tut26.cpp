#include<iostream>
using namespace std;

class complex
{
    int a,b;
    public:
    void SetNumber(int n1, int n2)
    {
        a=n1;
        b=n2;
    }
    friend complex sumcomplex (complex o1, complex o2);
    void PrintNumber(void)
    {
        cout<<"Your Number is "<<a<<" + "<<b <<"i"<<endl;
    }
};

complex sumcomplex(complex o1,complex o2)  // that is function which access the class object
{
    complex o3;
    o3.SetNumber((o1.a+ o2.a),(o1.b+o2.b));
    cout<<"----------------------"<<endl;
    return o3;
}
int main()
{
 complex c1,c2,sum;
 c1.SetNumber(1, 3);
 c1.PrintNumber();

 c2.SetNumber(2, 4);
 c2.PrintNumber();

sum = sumcomplex(c1, c2);
sum.PrintNumber();
return 0;
}