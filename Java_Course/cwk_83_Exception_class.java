package com.company;
//          Exception methods
//        1) Strings toString() executed when sout (e) is ran
//        2) Void printStackTrace() - prints Stack trace
//        3) String getMessage() - prints the exception message

import java.util.Scanner;

class MyException extends Exception{
    @Override
    public String toString() {
        return "I am toString()";
    }

    @Override
    public String getMessage() {
        return "I am getMessage()";
    }
}
class MaxAgeException extends Exception{
    @Override
    public String toString() {
        return "Age cannot be greater than 125";
    }

    @Override
    public String getMessage() {
        return "Make sure that the value of age entered is correct";
    }
}

public class cwk_83_Exception_class {

    public static void main(String[] args) {
        int a;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter age number");
        a = sc.nextInt();
        if (a<9){
            try{
//                 throw new MyException();   // custom exception   in main class
                  throw new MaxAgeException();
//                throw new ArithmeticException("This is an exception");  // built in
            }
            catch (Exception e){
                System.out.println(e.getMessage());
                System.out.println(e.toString());
                e.printStackTrace();
                System.out.println("Finished");
            }
            System.out.println("Yes Finished");
        }
    }

}
