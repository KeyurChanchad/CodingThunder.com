#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream kout("sample60.txt");
    string name;
    cout<<"Enter your name:"<<endl;
    cin>>name;
    kout<<name + " is my name.";
    kout.close();

    ifstream kin("sample60.txt");
    string st,st2;
    // kin>>st>>st2;
    getline(kin, st);
    cout<<"The content is "<<st<<endl;
    kin.close();
return 0;
}