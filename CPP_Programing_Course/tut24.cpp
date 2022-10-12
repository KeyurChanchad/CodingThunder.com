#include<iostream>
using namespace std;
class employee
{
    int id;
    static int count;
public:
    void setid()
    {
        cout<<"Enter Id of Employee:"<<endl;
        cin>>id;
        count++;
    }
    void getid()
    {
        cout<<"The Id of the employee is "<<id<<" and employee number is "<< count<<endl;
    }

    // if you want to access static datamember or function than create static function
    static void getcount(void)
    {
        cout<<"The value of count is "<<count<<endl;
    }
};

//count is static data member of class
// this is say that count is static data menber and static data is not declare in class
int employee::count = 1001;   //Default value is 0
// int employee::count;   

int main()
{
    employee keyur, akash, sagar;
    // keyur.id=101;
    // keyur.count=1;  // can't do this because it is private it throw error

    keyur.setid();
    keyur.getid();
    // keyur.getcount();
    employee::getcount();

    akash.setid();
    akash.getid();
    employee::getcount();

    sagar.setid();
    sagar.getid();
    employee::getcount();
    return 0;
}