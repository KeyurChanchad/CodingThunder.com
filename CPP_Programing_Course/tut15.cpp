#include<iostream>
using namespace std;

typedef struct employee
{
    int eId; //4
    char favChar; //1
    float salary; //4
} ep;

union money
{
    int rice; //4
    char car; //1
    float pounds; //4
};


int main(){
    // enum Meal{ breakfast, lunch, dinner};
    // Meal m1 = lunch;
    // cout<<(m1==0)<<endl;
    // cout<<breakfast<<endl;
    // cout<<lunch<<endl;
    // cout<<dinner<<endl;
    
    union money m1;
    m1.rice = 34;
    m1.car = 'c';
    cout<<m1.car <<sizeof(m1.rice)<<endl;
    cout<<m1.rice <<sizeof(m1.car)<<endl;

    // ep keyur;
    // struct employee shubham;
    // struct employee rohanDas;
    // keyur.eId = 1;
    // keyur.favChar = 'c';
    // keyur.salary = 120000000;
    // cout<<"The value is "<<keyur.eId<<endl; 
    // cout<<"The value is "<<keyur.favChar<<endl; 
    // cout<<"The value is "<<keyur.salary<<endl; 
    return 0;
}
