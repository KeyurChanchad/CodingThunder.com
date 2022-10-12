#include<iostream>
using namespace std;

// float funcAvg(int a, float b){
//     float avg = (a+b)/2;
//     return avg;
// }
// float funcAvg2(int a, int b){
//     float avg = (a+b)/2;
//     return avg;
// }

template <class T1, class T2>
float funcAvg(T1 a, T2 b){
    float res = (a+b)/2;
    return res;
}

template <class T>
void swapp(T &a, T &b){
    T tmp = a;
    a = b;
    b = tmp;
}

int main()
{
    float k = funcAvg(14.2, 8);
    printf("The Avarage of these number is %.2f\n",k);
    float x = 3.5, y = 2.9;
    swapp(x, y);
    cout<<x <<endl << y;
return 0;
}