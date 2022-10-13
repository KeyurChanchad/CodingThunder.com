package com.company;

class threadrunnable1 implements Runnable{
         int i =0;
        @Override
        public void run () {
            while(i <= 30)
            {
                System.out.println("I am Runnable interface 1 in Thread Class 1 ");
                i++;
            }
        }
}
class threadrunnable2 implements Runnable{
    int i =0;
        @Override
        public void run () {
            while( i <= 40)
            {
                System.out.println("Class 2 of Runnnable thread 2");
                i++;
             }
         }
}
public class cwk_71_Runnable_Thread {
    public static void main(String[] args) {

        threadrunnable1 bullet1 = new threadrunnable1();
        Thread gun1 = new Thread(bullet1);

        threadrunnable2 bullet2 = new threadrunnable2();
        Thread gun2 = new Thread(bullet2);

//        bullet1.start();
        gun1.start();
        gun2.start();
//        gun1.run();
//        gun2.run();
    }
}
