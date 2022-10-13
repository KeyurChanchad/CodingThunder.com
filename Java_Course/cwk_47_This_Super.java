package com.company;

import javax.print.Doc;

class EkClass{
    private int a;

    EkClass(int a){
        this.a = a;
    }

    public int getA() {
        return a;
    }

    public int returnone(){
        return 1;
    }
}

class DoClass extends EkClass{
    DoClass(int c){
        super(c);
        System.out.println("I am a of derived class constructor");
    }
}

public class cwk_47_This_Super {

    public static void main(String[] args) {
        EkClass e = new EkClass(65);
        DoClass d = new DoClass(5);
        System.out.println(e.getA());
    }

}
