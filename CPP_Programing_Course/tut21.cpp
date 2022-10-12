#include<iostream>
using namespace std;
class employee
{
    private:
    int a,b,c;
    public:
    int d,e;
    void setdata(int x, int y, int z); //Declaration
    void getdata()
    {
        cout<<"The value of a is "<<a<<endl;
        cout<<"The value of b is "<<b<<endl;
        cout<<"The value of c is "<<c<<endl;
        cout<<"The value of d is "<<d<<endl;
        cout<<"The value of e is "<<e<<endl;
    }
};
 void employee :: setdata(int x, int y, int z)
 {
     a=x;
     b=y;
     c=z;
 }
int main()
{
    employee keyur;
    // keyur.a=16; //This will throw errer as it is private
    keyur.d=95;
    keyur.e=2013;
    keyur.setdata(22,99,53);
    keyur.getdata();

return 0;
}