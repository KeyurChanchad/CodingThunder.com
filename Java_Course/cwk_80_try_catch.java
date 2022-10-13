package com.company;

import java.text.NumberFormat;

public class cwk_80_try_catch {

    public static void main(String[] args) {
        int a = 6000;
        int b = 0;
        // Without Try:
//        int c = a / b;
//        System.out.println("The result is " + c);

        // All The Exception in Java.lang
        // Builtin Exception
//            ~ArithmeticException
//            ~ArrayIndexOutOfBoundsException
//            ~NumberFormat
//            ~NullPointerException
        // With Try:
        try {
            int c = a / b;
            System.out.println("The result is " + c);
        }
        catch(Exception e) {
            System.out.println("We failed to divide. Reason: ");
            System.out.println(e);
        }
        System.out.println("End of the program");
    }
}
