package com.company;

public class cwk_35_PS7_methods {
        //problem 1
        static void multiplication(int n) {
            for (int i = 1; i <= 10; i++) {
                System.out.format("%d X %d = %d\n", n, i, n * i);
            }
        }

        //problem 2
        static void pattern1(int n) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < i + 1; j++) {
                    System.out.print("*");
                }
                System.out.println();
            }
        }

    //problem 3
    // sum(n) = 1 + 2 + 3... + n
    // sum(n) = 1 + 2 + 3... + n-1 + n
    // sum(n) = sum(n-1) + n
    // sum(3) = 3 + sum(2)
    // sum(3) = 3 + 2 + sum(1)
    // sum(3) = 3 + 2 + 1
    static int sumRec(int n) {
        // Base condition
        if (n == 1) {
            return 1;
        }
        return n + sumRec(n - 1);
    }

        //Problem 4
        static void print_star_iterative(int n)
        {
            for (int j = 0; j < n ; j++)
            {
                for (int k = 0; k < n-j; k++)
                {
                    System.out.print("* ");
                }
                System.out.println();
            }
        }

        //Problem 5
        static int fib(int n) {
        /* if(n==1){
            return 0;
        }
        else if(n==2){
            return 1;
        } */
            if (n == 1 || n == 2) {
                return n - 1;
            } else {
                return fib(n - 1) + fib(n - 2);
            }
        }
    // Problem 6
    static int sum(int ...arr)
    {
        int sum = 0;
        for(int e : arr)
        {
            sum += e;
        }
        return sum;
    }

    //Problem 7
    static void pattern1_rec(int n) {
        if (n > 0) {
            pattern1_rec(n - 1);
            for (int i = 0; i < n; i++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
    // pattern1_rec(3)
    // pattern1_rec(2) + 3 times star and new line
    // pattern1_rec(1) + 2 times star and new line + 3 times star and new line
    // pattern1_rec(0) + 1 times star and new line + 2 times star and new line + 3 times star and new line

    //Problem 8
    static void pattern2_rec(int n) {
        if (n > 0) {
            for (int i = 0; i < n; i++) {
                System.out.print("* ");
            }
            System.out.println();
            pattern2_rec(n - 1);
        }
    }

        //problem 9
        static void temperature(float c){
            float f;
            f = (c * 9/5) + 32;
            System.out.println("Fahrenheit is : " + f);
        }
    //Problem 10
    static void sum_iteretive(int n)
    {
        int sum = 0;
        for(int k = 1; k <= n; k++)
        {
            sum += k;
        }
        System.out.println("The sum of the n natural number " + sum);
    }

        public static void main(String[] args) {
            // Problem 1
             multiplication(7);

            // Problem 2
             pattern1(9);

            // Problem 3
             int c = sumRec(4);
             System.out.println(c);

            //Problem 4
            print_star_iterative(4);

            // Problem 5
            // fibonacci series - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
             int result = fib(7);
             System.out.println(result);

            //Problem 6
            int s = sum(5, 7, 3, 2 ,3);
            System.out.println("The sum varargs " + s);

            //Problem 7
            pattern1_rec(5);

            // Problem 8
            pattern2_rec(9);

            //problem 9
            temperature(3.5f) ;
            //Problem 10
             sum_iteretive(5);
        }
    }


