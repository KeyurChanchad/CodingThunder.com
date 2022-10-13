package com.company;

interface MyCamera{
    void takeSnap();
    void recordVideo();  //----> must be declare like this
    //private does not inherit so it put into the function
    private void greet(){
        System.out.println("Good Morning");
    }  //---> Here It define
    default void record4KVideo(){       //---> Here It also define
        greet();
        System.out.println("Recording in 4k...");
    }
}

interface MyWifi{
    String[] getNetworks();
    void connectToNetwork(String network);
}

class MyCellPhone{
    void callNumber(int phoneNumber){
        System.out.println("Calling "+ phoneNumber);
    }
    void pickCall(){
        System.out.println("Connecting... ");
    }

}

class MySmartPhone extends MyCellPhone implements MyWifi, MyCamera{
    public void takeSnap(){
        System.out.println("Taking snap...");
    }
    public void recordVideo(){
        System.out.println("Record video...");
    }
    public void record4KVideo(){
        System.out.println("Taking snap and recoding in 4k");
    }
    public String[] getNetworks(){
        System.out.println("Getting List of Networks");
        String[] networkList = {"Localhost", "oppo k10", "Anjali5G"};
        return networkList;
    }
    public void connectToNetwork(String network){
        System.out.println("Connecting to " + network);
    }
}

public class cwk_57_Default_Method {

    public static void main(String[] args) {
        MySmartPhone ms = new MySmartPhone();
        ms.record4KVideo();
        // ms.greet(); --> Throws an error! because of private
        String[] ar = ms.getNetworks();
        for (String item : ar) {
            System.out.println(item);
        }
        ms.takeSnap();
        ms.callNumber(926942626);
    }
}
