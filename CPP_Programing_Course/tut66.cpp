#include<iostream>
using namespace std;
template <class T1=int, class T2=char, class T3=float>
class keyur{
        T1 a;
        T2 b;
        T3 c;
     public: 
        keyur(T1 x, T2 y, T3 z){
            a = x;
            b = y; 
            c = z;
        }
        void display(){
            cout<<a<<endl;
            cout<<b<<endl;
            cout<<c<<endl<<endl;
        }
};
int main()
{
    keyur <> k1(12, 'g', 23.12);
    k1.display();
    keyur <float, char, char> k2(52.13, 'c', 'K');
    k2.display();
return 0;
}