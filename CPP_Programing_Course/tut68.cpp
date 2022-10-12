#include<iostream>
using namespace std;
template <class T>
class keyur{
     public:
       T data;
       keyur(T a){
           data =  a;
       } 
       void display();
};
template <class k>
void keyur<k> :: display(){
    cout<<data <<endl;
}

void func(int a){
    cout<<"I am first func() "<<a <<endl;
}

template <class f>
void func(f b){
    cout<<"i'm template func()...! "<<b<<endl;
}
int main()
{
    // keyur<char> ck('C');
    // keyur<int> ck(12);
    // keyur<float> ck(32.15);
    // ck.display();
    // cout<<ck.data<<endl;

    func(9);
    func(85.22);
    func('W');
return 0;
}