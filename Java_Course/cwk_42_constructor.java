package com.company;

class MyMainEmployee{
    private int id;
    private String name;
    // Constructor name same as class name. This is default constructor
    public MyMainEmployee(){
        id = 0;
        name = "Your-Name-Here";
    }
//    This is parameterize constructor
    public MyMainEmployee(String myName, int myId){
        id = myId;
        name = myName;
    }
    public MyMainEmployee(String myName){
        id = 1;
        name = myName;
    }
    public String getName(){
        return name;
    }
    public void setName(String n){
        this.name = n;
    }
    public void setId(int i){
        this.id = i;
    }
    public int getId(){
        return id;
    }
}


public class cwk_42_constructor {

        public static void main(String[] args) {
//            Constructor is special function when object of class initialize it will invoke.
            //MyMainEmployee keyur = new MyMainEmployee("ProgrammingWithKeyur", 12);
            //MyMainEmployee chanchad = new MyMainEmployee();
            MyMainEmployee chanchad = new MyMainEmployee("Keyur");
//            chanchad.setName("CodeWithKeyur");
//            chanchad.setId(22);
            System.out.println(chanchad.getId());
            System.out.println(chanchad.getName());
        }
}

