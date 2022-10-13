package com.company;

public class CWK_09_ch2_opr_precedence {

    public static void main(String[] args) {

                // Precedence & Associativity
                // Associativity means left to right or right to left
                //Precedence means priority
                //int a = 6*5-34/2;
                //System.out.println(a);

        /*
        Highest precedence goes to * and /. They are then evaluated on the basis of
        left to right associativity
            =30-34/2
            =30-17
            =13
         */
                //int b = 60/5-34*2;
                //System.out.println(b);

        /*
            = 12-34*2
            =12-68
            =-56
         */


                // Quick Quiz
                int x = 6;
                int y = 1;
                //  int k = x * y/2;

                int b = 0;
                int c = 0;
                int a = 10;
                int k = ( b*b - (4*a*c) )/(2*a);
                System.out.println(k);

                int v = 6 , u = 3;
                 System.out.println(v*v - u*u);

                 int d = 8, e = 5;
                System.out.println(a * e - d);
    }
}
