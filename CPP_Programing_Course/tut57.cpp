#include<iostream>
using namespace std;
class CWH{
    protected:
        string title;
        float rating;
    public:
        CWH(string s, float r){
            title =  s;
            rating = r;
        }
        virtual void display(){
            cout<<"Base class display function called:"<<endl;
        }
};

class CWHvideo: public CWH{
    float videolength;
    public:
        CWHvideo(string s,float r,float vl): CWH(s,r){
            videolength = vl;
        }
        void display(){
            cout<<"This is an amazing video with title  "<<title <<endl;
            cout<<"Rating  "<<rating <<" out of 5 stars"<<endl;
            cout<<"Length of the video is "<<videolength <<" minites"<<endl;
        }
};
class CWHText: public CWH
{
    int words;
    public:
        CWHText(string s, float r, int wc): CWH(s, r){
            words = wc;
        }
     void display(){
      cout<<"This is an amazing text tutorial with title "<<title<<endl;
      cout<<"Ratings of this text tutorial: "<<rating<<" out of 5 stars"<<endl;
      cout<<"No of words in this text tutorial is: "<<words<<" words"<<endl;
         }
};

int main()
{
    // CWH cpp("keyur",2.3);
    // cpp.display();
    // CWHvideo oops("harry",4.5,20.23);
    // oops.display();
    //  CWH *ptr;
    //  ptr = &oops;
    //  ptr->display();

    string title = "Django tutorial";
    float rating =4.69;
    float videolength = 20.16;
    int words = 450;

    CWHvideo djvideo(title,rating,videolength);
    // djvideo.display();

    title = "DJ text";
    rating = 4.20;
    words = 436;
    CWHText djtext(title,rating,words);
    // djtext.display();

    CWH *tuts[2];
   tuts[0] = &djvideo;
   tuts[1] = &djtext;

    tuts[0]->display();
    tuts[1]->display();
return 0;
}