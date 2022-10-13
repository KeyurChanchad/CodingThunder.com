package com.company;
/*
There are three types of errors in java.
        1) Syntax errors
        2) Logical errors
        3) Runtime errors- also called Exceptions


        1) Syntax Errors
        When complex finds something wrong with our program,

        it throws a syntax error

        int   a = 9  // No semicolon, syntax errors!
        a =   a + 3;
        d = 4; // Variable not declared, syntax errors

2)Logical errors
A logical error or a bug occurs when a program compiles and round but does the wrong thing.

- Message delivered wrongly
- Wrong time of chats being displayed
- Incorrect redirects!

3)Runtime errors:
Java may sometimes encounter an error while the program is running.
These are also called Exceptions!
These are encountered due to circumstances like bad input and (or) resource constraints.

 */
public class cwk_78_Error {

        public static void main(String[] args) {
            int a = 5;
            int b = 9;
            System.out.println(a+b);
        }
}

