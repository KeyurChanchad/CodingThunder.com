#include<iostream>
using namespace std;
template <class T1, class T2>
class myclass{
    T1 x;
    T2 y;
    public:
    myclass(T1 a, T2 b){
        x = a;
        y = b;
    }
    void display(){
        cout<<this->x <<endl;
        cout<<this->y <<endl;
    }
};
int main()
{
    // myclass <char,int> obj('K',999);
    myclass <float,double> obj(12.36,9145299);
    obj.display();
return 0;
}   