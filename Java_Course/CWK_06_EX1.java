package com.company;

import java.util.Scanner;

public class CWK_06_EX1 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Your sub 1 marks:");
        byte s1 = sc.nextByte();

        System.out.println("Enter Your sub 2 marks:");
        byte s2 = sc.nextByte();

        System.out.println("Enter Your sub 3 marks:");
        byte s3 = sc.nextByte();

        System.out.println("Enter Your sub 4 marks:");
        byte s4 = sc.nextByte();

        System.out.println("Enter Your sub 5 marks:");
        byte s5 = sc.nextByte();

        float sum = s1 + s2 + s3 + s4+ s5;
        float percentage = (sum / 500.0f) * 100 ;

        System.out.println("The Percentage of these marks: " + percentage);
    }
}
