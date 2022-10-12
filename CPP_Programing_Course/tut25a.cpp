#include<iostream>
using namespace std;

class Employee
{
    int id; 
    int salary;
    public:
    void setId(void)
    {
        salary=122;
        cout<<"Enter ID of Employee:"<<endl;
        cin>>id;
    }
    void getId(void)
    {
        cout<<"The Id of the Employee is "<<id<<endl;
    }
};
int main()
{
    // Employee keyur,bhisma,arjun,bheem;
    // keyur.setId();
    // keyur.getId();

    Employee mb[4];                 // Array of the Object
    for (int i = 0; i < 4; i++)
    {
        mb[i].setId();
        mb[i].getId();
    }
    
return 0;
}