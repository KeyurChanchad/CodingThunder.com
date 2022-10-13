//First of all make class inside main method in java.
//in terminal type javac yourfilename javac is compiler then java .class
// file that is your class name of main method

/*
Data types in Java fall under the following categories

 1)Primitive Data Types (Intrinsic)
 2)Non-Primitive Data Types (Derived)
 There are 8 primitive data types supported by Java:

byte     ➼   •value ranges from -128 to 127
                  •takes 1 byte
                  •default value is 0

short    ➼   •value ranges from -(216)/2  to  (216)/2 - 1
                   •takes 1 byte
                   •default value is 0

int        ➼    •value ranges from -(232)/2 to (232)/2 - 1
                    •takes 2 byte
                    •deafault value is 0

float      ➼    •value ranges from (see Docs)
                    •takes 4 byte
                    •deafault value is 0.0f

long      ➼    •value ranges from -(264) /2 to (264)/2 - 1
                    •takes 8 byte
                    •default value is 0

double   ➼  •value ranges from (see Docs)
                   •takes 8 byte
                   •deafault value is 0.0d

char       ➼  •value ranges from 0 to 65535(216 - 1)
                    •takes 2 byte
                    •default value is

boolean ➼   •value can be true or false
                    •1 byte size depend on JVM
                    •default value is false
 */

package com.company;

public class CWK_04_literals {

    public static void main(String[] args) {
        byte age = 34;
        int age2 = 56;
        short age3 = 87;
        long ageDino = 5666666666666L;
        char ch = 'A';
        float f1 = 5.6f;
        double d1 = 4.66;   // Double is  Default
        boolean a = true;
        String str = "Keyur Chanchad";

        System.out.println(age);
        System.out.println(age2);
        System.out.println(age3);
        System.out.println(ageDino);
        System.out.println(ch);
        System.out.println(f1);
        System.out.println(d1);
        System.out.println(str);

    }
}
