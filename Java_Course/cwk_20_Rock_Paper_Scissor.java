package com.company;

import java.util.Scanner;
import  java.util.Random;

public class cwk_20_Rock_Paper_Scissor {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       int mych, mycount = 0, comcount =0;

        for (int i=1; i<=5; i++) {
           System.out.println("\n1.Rock");
           System.out.println("2.Paper");
           System.out.println("3.Scissor");
           System.out.print("Enter your choice: ");
           mych = sc.nextInt();
//        System.out.println(mych);
           if (mych == 1) {
               System.out.println("You : Rock");
           }
           else if (mych == 2) {
               System.out.println("You : Paper");
           }
           else if(mych == 3)
               System.out.println("You : Scissor");
           else {
               System.out.println("Invalid choice :");
               break;
           }

//          Rondom variable
           Random r = new Random();
           int c = r.nextInt(3);
//        System.out.println(c);

           if (c == 0) {
               System.out.println("computer : Rock");
           }
           else if (c == 1) {
               System.out.println("computer : Paper");
           }
           else if( c == 2 )
               System.out.println("computer : Scissor");

           //------------------------------------------------------
            // comparison
           if (mych == 1 && c == 0 || mych == 2 && c == 1 || mych == 3 && c == 2) {
               System.out.println("Draw");
           }
           else if (mych == 1 && c == 1 || mych == 2 && c == 2 || mych == 3 && c == 0) {
               System.out.println("Computer win");
               comcount += 1;
           }
           else if (mych == 1 && c == 2 || mych == 2 && c == 0 || mych == 3 && c == 1) {
               System.out.println("You win");
               mycount += 1;
           }
            else
               System.out.println("Invalid Command!!!!!");
       }

       if (mycount > comcount){
        System.out.println("\nYou are winner.....");
       }
       else if (comcount > mycount){
           System.out.println("\nComputer Win The game....");
       }
       else
           System.out.println("\nThe match is Draw......");
    }
}
