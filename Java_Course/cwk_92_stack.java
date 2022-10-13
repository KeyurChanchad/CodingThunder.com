package com.company;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

//The stack is the subclass of Vector. It implements the last-in-first-out data structure, i.e., Stack. The stack contains all of the methods of Vector class and also provides its methods like boolean push(), boolean peek(), boolean push(object o), which defines its properties.
public class cwk_92_stack {
    public static void main(String[] args) {
        Stack s = new Stack();

        s.add("Keyur");
        s.push(15);
        s.set(0, 16.35);
        s.push("Ankit");
        s.push("Vishal");
        System.out.println(s.isEmpty());
        System.out.println(s.peek());
        System.out.println(s.contains(15));
        System.out.println(s.pop());
        System.out.println(s.search("Keyur"));

        System.out.println(s);


    }
}
