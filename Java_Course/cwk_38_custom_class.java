package com.company;

class Employee{
    //class member or properties
    int id;
    int salary;
    String name;
    //class method
    public void printDetails(){
        System.out.print("My id is " + id + " and my name is "+ name);
    }

    public int getSalary(){
        return salary;
    }

//    public String toString(){
//        System.out.println("You have invoke toString method of Emp that is override.");
//    }
}
public class cwk_38_custom_class {

        public static void main(String[] args) {
            System.out.println("This is our custom class");
            Employee keyur = new Employee(); // Instantiating a new Employee Object
            Employee john = new Employee(); // Instantiating a new Employee Object

//            Any class object return className@hashCode. Basically it automatically call toString().
            System.out.println(keyur);  //com.company.Employee@6d03e736
            // Setting Attributes for keyur
            keyur.id = 12;
            keyur.salary = 34;
            keyur.name = "CodingThunder";

            // Setting Attributes for John
            john.id = 17;
            john.salary = 12;
            john.name = "John Khandelwal";

            // Printing the Attributes
            keyur.printDetails();
            john.printDetails();
            int salary = john.getSalary();
            System.out.println(salary);
            // System.out.println(keyur.id);
            // System.out.println(keyur.name);
        }
    }

