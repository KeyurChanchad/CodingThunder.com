package com.company;

class NegativeRadiusException extends Exception{
    @Override
    public String toString() {
        return "RADIUS cannot be negative!";
    }

    @Override
    public String getMessage() {
        return "radius cannot be negative!";
    }
}

public class cwk_84_throw_throws {

        public static double area(int r) throws NegativeRadiusException{   // it may be throw error
            if (r<0){
                throw new NegativeRadiusException();    //  in other method
            }
            double result = Math.PI * r * r;
            return result;
        }
        public static int divide(int a, int b) throws ArithmeticException{
            // Made By Keyur
            int result = -1;
            try {
                result = a/b;
                return result;
            }
            catch (ArithmeticException e){
                System.out.println("ArithmeticException Occurred");
            }
            return result;
        }

    public static void main(String[] args) throws NegativeRadiusException {
            double area = area(3);
        System.out.println("Area is " + area);

        int result = divide(4,0);
        System.out.println(result);

    }
}
