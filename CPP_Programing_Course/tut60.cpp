#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    string st="code With Keyur";
    // Opening files using constructor and writing it
    string st2;     // Write operation
    ofstream pro_out("sample60.txt");
    pro_out<<st;
    // cout<<st<<endl;
    pro_out.close();

    // Opening files using constructor and Reading it
    ifstream innn ("sample60b.txt");  // read file
    // innn>>st2;
    getline(innn,st2);
    getline(innn,st2);
    cout<<st2;
return 0;
}


