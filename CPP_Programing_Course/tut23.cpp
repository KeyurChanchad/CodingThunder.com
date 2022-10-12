#include<iostream>
using namespace std;

class shope
{
    int itemid[10];
    int price[10];
    int counter;              // int counter=0; it not use
public:
    void intcounter(void)
    {
        counter=0;
    }
    void setdata(void);
    void displaydata(void);
};

void shope::setdata(void)
{
    cout<<"Enter ID of your item NO :"<<counter+1<<endl;
    cin>>itemid[counter];
    cout<<"Enter price of your item:"<<endl;
    cin>>price[counter];
    counter++;
}
void shope::displaydata(void)
{
    for (int i = 0; i < counter; i++)
    {
        cout<<"The price of item with ID "<<itemid[i]<<" is "<<price[i]<<endl;
    }
}
int main()
{
    int i, n;
    shope dukkan;
//    int  counter=0;           // this is not recommened it reserve space in memory Entire program
    dukkan.intcounter();
    // dukkan.setdata();
    // dukkan.setdata();
    // dukkan.setdata();
    cout<<"Enter Number of item you wan to store:"<<endl;
    cin>>n;
    for (i = 0; i < n; i++)
    {
        dukkan.setdata();

    }

    dukkan.displaydata();
    return 0;
}