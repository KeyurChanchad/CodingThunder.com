package com.company;

public class cwk_33_variable_argument {

    /*
    static int sum (int a, int b)
    {
        return  a  + b;
    }static int sum (int a, int b, int c)
    {
        return  a  + b + c;
    }static int sum (int a, int b, int c, int d)
    {
        return  a + b +c +d;
    }
    */

    static int sum (int k, int ...arr)
    {
        int sum = 0 ;
        for (int a: arr)
        {
            sum += a;
        }
        return sum;
    }

    public static void main(String[] args) {
        /*
            public static void foo(int … arr)
            {
               arr is available here as int[] arr
            }

        public static void bar(int a, int arr){
              Code
        }
         */

        System.out.println("Welcome to varargs :");
//        System.out.println("The sum of 0 argument: " + sum());
        System.out.println("The sum of 1 argument: " + sum(1));
        System.out.println("The sum of 1 , 2 is " +  sum(1,2) );
        System.out.println("The sum of 1 , 2, 3  is " +  sum(1,2, 3) );
        System.out.println("The sum of 1 , 2,3 ,4 is " +  sum(1,2, 3 , 4) );

    }
}
