package com.company;

class StaticDemo{
//    int id = 18;
//    String name = "Keyur";

    // Only one copy of static variable are assign to all object.
    static int id = 18;
    static String name = "Keyur";
    static int counter = 0;

    //static method
    static void showCounter() {
        counter++;
        System.out.println(counter);
    }
}
public class CWK_37_Static {
    public static void main(String[] args) {
        //If we want to access methods and properties directly without creating an object of class so less occupying space in memory then it must be static. You can also access by an object.

        StaticDemo sd = new StaticDemo();
//        System.out.println(sd.id + " " + sd.name);

//        System.out.println(StaticDemo.id + " " + StaticDemo.name);

//        sd.showCounter(); //normal method can invoke static variable
        StaticDemo.showCounter(); // static method can't invoke Non-static method it must be static

        StaticDemo sd1 = new StaticDemo();
        sd.showCounter();
    }
}
