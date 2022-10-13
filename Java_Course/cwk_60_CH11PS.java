package com.company;

abstract class Pen{
    abstract void write();
    abstract void refill();
}

class FountainPen extends Pen{
    void write(){
        System.out.println("Write");
    }
    void refill(){
        System.out.println("Refill");
    }
    void changeNib(){
        System.out.println("Changing the nib");
    }
}
class Monkey{
    void jump(){
        System.out.println("Jumping...");
    }
    void bite(){
        System.out.println("Biting...");
    }
}

interface BasicAnimal{
    void eat();
    void sleep();
}

class Human extends Monkey implements BasicAnimal{
    void speak(){
        System.out.println("Hello sir!");
    }

    @Override
    public void eat() {
        System.out.println("Eating");
    }

    @Override
    public void sleep() {
        System.out.println("Sleeping");
    }
}

abstract  class telephone {
    abstract void ring();
    abstract void light();
    abstract void disconnect();
}

class smartphone extends telephone{
    @Override
    void ring() {
        System.out.println("ringing.....");
    }

    @Override
    void disconnect() {
        System.out.println("Phone has disconnect");
    }

    @Override
    void light() {
        System.out.println("Light is on..");
    }
}

interface tvremote {
    void channel(String channel);
    void connection();
}
interface smartTvremote extends tvremote{
    void channel(String channel);
    void connection();
    void setwithcomputer();
    void showmobilescreen();
}

class tv implements smartTvremote{

       public void channel(String channel){
        System.out.println("Channel is " + channel);
    }
    public void connection(){
        System.out.println("Connection is successfully");
    }
    @Override
    public void setwithcomputer(){
        System.out.println("Tv is connected with computer.");
    }

    @Override
    public void showmobilescreen() {
        System.out.println("Now your smartphone presenting");
    }
}

public class cwk_60_CH11PS {

    public static void main(String[] args) {
        // Q1 + Q2
        FountainPen pen = new FountainPen();
        pen.changeNib();

        // Q3
        Human key = new Human();
        key.sleep();

        // Q5
        Monkey m1 = new Human();
        m1.jump();
        m1.bite();
        // m1.speak(); --> Cannot use speak method because the reference is monkey which does not have speak method

        BasicAnimal lovish = new Human();
        // lovish.speak(); --> error
        lovish.eat();
        lovish.sleep();

        smartphone sm = new smartphone();
        sm.disconnect();
        sm.ring();

        tv tv = new tv();
        tv.channel("TV 9");
        tv.connection();
        tv.setwithcomputer();
        tv.showmobilescreen();

    }
}
