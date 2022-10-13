package com.company;

abstract class Parent2{
    public Parent2(){
        System.out.println("Mai parent2 ka constructor hoon");
    }
    public void sayHello(){
        System.out.println("Hello");
    }
    //1. When any class derived from this class at that time these method must be override.
    //2. or derived class declare it self as abstract
    // In both of case you declare method as abstract.
    //Abstract method has no body. One abstract method make whole class as abstract
    // You can not declare abstract class object
    abstract public void greet();
    abstract public void greet2();
}

class Class2 extends Parent2 {

    @Override
    public void greet(){
        System.out.println("Good morning");
    }
    @Override
    public void greet2(){
        System.out.println("Good afternoon");
    }
}

abstract class Child3 extends Parent2{
    public void th(){
        System.out.println("I am good");
    }
}

class Grandchild extends  Child3
{
    @Override
    public void greet() {
    }
    @Override
    public void greet2() {
    }
}
public class cwk_53_abstract {

    public static void main(String[] args) {
//        Parent2 p = new Parent2(); // -- error you can't create abstract class object
//        Child2 c = new Child2();
//        Child3 c3 = new Child3(); -- error
    }
}
