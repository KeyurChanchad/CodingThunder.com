package com.company;

//interface have abstract and non abstract method.
// interface's abstract method doesn't have body.
//That must be override
interface Bicycle{
    int a = 45;
    void applyBrake(int decrement);
    void speedUp(int increment);
}

interface HornBicycle{
    int x = 66;
    void blowHornK3g();
    void blowHornM23();
}

//class implements one or more interface and must have override all method.
class AvonCycle implements Bicycle, HornBicycle{
    //public int x = 5;
    void blowHorn(){
        System.out.println("Pee Pee Poo Poo");
    }
    public void applyBrake(int decrement){
        System.out.println("Applying Brake");
    }
    public void speedUp(int increment){
        System.out.println("Applying SpeedUP");
    }
    public void blowHornK3g(){
        System.out.println("Kabhi khushi kabhi gum pee pee pee pee");
    }

    @Override
    public void blowHornM23() {
        System.out.println("Horn M23 method of hornBicycle interface");
    }

}

public class cwk_54_Interfaces {
    public static void main(String[] args) {
        AvonCycle cycle = new AvonCycle();
        cycle.applyBrake(1);
        cycle.speedUp(12);
        // You can create properties in Interfaces
        System.out.println(cycle.a);
        System.out.println(cycle.x);

        // You cannot modify the properties in Interfaces as they are final
//         cycle.a = 454;
        //System.out.println(cycle.a);

        cycle.blowHornK3g();
        cycle.blowHornM23();
    }
}
