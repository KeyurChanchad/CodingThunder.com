#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream out;
    out.open("sample60.txt");
    out<<"Keyur is my name\n";
    out<<"I'am programmer"<<endl;
    out<<"Now, i am working on file";
    out.close();

    ifstream in;
    in.open("sample60.txt");
    string st,st2;
    // in>>st>>st2;
    // cout<<st<<st2<<endl;
    while(in.eof() == 0){
        getline(in, st);
        cout<<st<<endl;
    }
    in.close();
return 0;
}