package com.company;

//import java.util.Scanner;  //------>1.
import java.util.*;       //---->2.

public class cwk_65_Packages {

    public static void main(String[] args) {
        System.out.println("Enter number:");
        Scanner sc = new Scanner(System.in);   //----->1.  2.
        // java.util.Scanner sc = new java.util.Scanner(System.in);  //---->3.
        int a = sc.nextInt();
        System.out.println("This is my scanner taking input as " + a);
    }
}
