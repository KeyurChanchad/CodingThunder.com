package com.company;

//public class dog extends Animal {
//     code
//}
class Base{
    public int x;

    public int getX() {
        return x;
    }

    public void setX(int x) {
        System.out.println("I am in base and setting x now");
        this.x = x;
    }

    public void printMe(){
        System.out.println("I am a method of base class.");
    }
}

class Derived extends Base{
    public int y;

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}
public class cwk_45_Inheritance {
//        Single Inheritance
//        MultiLevel Inheritance
//        Hierarchycal Inheritance
//        Hybride Inheritance
//          Java doesn't support Multiple Inheritance so interface concept appear.
        public static void main(String[] args) {
            // Creating an Object of base class
            Base b = new Base();
            b.setX(4);
            System.out.println(b.getX());

            // Creating an object of derived class
            Derived d = new Derived();
            d.setY(43);
            System.out.println(d.getY());
            //derived class obj can access base class member and method
            System.out.println(d.getX());
        }
    }


