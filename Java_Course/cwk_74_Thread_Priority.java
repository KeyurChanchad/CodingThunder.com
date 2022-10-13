package com.company;

class MyThr1 extends Thread{
    public MyThr1(String name){
        super(name);
    }
    public void run(){
        int i = 1;
        while(i < 10){
//            System.out.println("I am a thread");
            System.out.println("Thank you: " + this.getName());
            i++;
        }
    }
}


public class cwk_74_Thread_Priority {
    public static void main(String[] args) {
        // Ready Queue: T1 T2 T3 T4 T5
        MyThr1 t1 = new MyThr1("Keyur1");
        MyThr1 t2 = new MyThr1("Keyur2");
        MyThr1 t3 = new MyThr1("Keyur3");
        MyThr1 t4 = new MyThr1("Keyru4");
        MyThr1 t5 = new MyThr1("Keyur5 (most Important)");
        t5.setPriority(Thread.MAX_PRIORITY);   //10
        t1.setPriority(Thread.MIN_PRIORITY);   //1
        t2.setPriority(Thread.NORM_PRIORITY);  // 5
        t3.setPriority(Thread.MIN_PRIORITY);  // 1
        t4.setPriority(Thread.NORM_PRIORITY);   // 5
        t5.setPriority(Thread.MIN_PRIORITY);  // 1
        //t1.setPriority(5);
//    t1.setPriority(540)
        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();
    }
}
