package com.company;

class MyThread1 extends Thread{
    @Override  // This decorator for knowing this method is override.
    public void run(){
        int i =0;
        while(i<10){
            System.out.println("My Cooking Thread is Running");
            System.out.println("I am happy!");
            i++;
        }
    }
}

class MyThread2 extends Thread{
    @Override
    public void run(){
        int i =0;
        while(i<5){
            System.out.println("Thread 2 for Chatting with her");
            System.out.println("I am sad!");
            i++;
        }
    }
}


public class cwk_70_Thread_class {

    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();
        t1.start(); //when thread start it gives sometime to t1 and t2.
        t2.start();
//        t1.run();
//        t2.run();
    }
}
