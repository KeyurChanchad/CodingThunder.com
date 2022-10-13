package com.company;
//CONSTRUCTORS
//        Thread ( )
//        Thread ( string )
//        Thread ( Runnable r )
//        Thread ( Runnable r, String name )

class MyThr extends Thread{
    public MyThr(String name){
        super(name);
    }
    public void run(){
        int i = 34;
        System.out.println("Thank you");
//        while(true){
//            System.out.println("I am a thread");
//        }
    }
}
class runint implements Runnable{
    @Override
    public void run() {
        System.out.println("This is runnable interface.");
    }
}

public class cwk_73_Thread_Constructor {

    public static void main(String[] args) {
        MyThr t1 = new MyThr("Keyur");
        MyThr t2 = new MyThr("Ankit");
        t1.start();
        t2.start();
        System.out.println("The id of the thread t1 is " + t1.getId());
        System.out.println("The name of the thread t1 is " + t1.getName());
        System.out.println("The id of the thread t2 is " + t2.getId());
        System.out.println("The name of the thread t2 is " + t2.getName());

        runint ri = new runint();
        Thread rit= new Thread(ri, "Keyur Chanchad");
        System.out.println("The name of thread "+ rit.getName());
        System.out.println("The id of thread "+ rit.getId());

    }
}
