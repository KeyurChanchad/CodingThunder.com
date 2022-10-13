package com.company;

class  FinalDemo{
    String name;
    FinalDemo(String name){
        this.name = name;
    }
    void  showName(){
        System.out.println("Name " + this.name);
    }
}
public class CWK_37_Final {
    public static void main(String[] args) {
        //You can reinitialize variable and object but if it final you can't change it.
        //Same as you can reinitialize method and class but you can't override and inherit approximately.
        final int x = 10;
        System.out.println(x);

        // x = 20; // You can not reassign variable due to its final
//        System.out.println(x);

        final FinalDemo fd =new FinalDemo("Keyur");
        fd.showName();

//        fd = new FinalDemo("Pritam");
//        fd.showName();

        FinalDemo fd1 = new FinalDemo("Ankit");
        fd1.showName();

    }
}
