package com.company;
import java.util.*;
import java.util.ArrayList;

// Use java 14 docs oracle official
//The ArrayList class implements the List interface. It uses a dynamic array to store the duplicate element of different data types. The ArrayList class maintains the insertion order and is non-synchronized. The elements stored in the ArrayList class can be randomly accessed.

public class cwk_91_ArrayLIst {

        public static void main(String[] args) {
//              By default initialCapacity 10. When objects are goes out of initial capacity then it will increase 50% of it's size.
            List al1 = new ArrayList();//Creating arraylist

//            <> This is Generic where we define specific type of object allow.It can be Integer, String, Employee, Car.
            ArrayList<Integer> al2 = new ArrayList<>(5);
            ArrayList<String> str = new ArrayList<String>(15);

            System.out.println(al1.size());
            System.out.println(al1.isEmpty());

            al1.add(6); //Adding object in arraylist
            al1.add(86.15);
            al1.add("Keyur");
            al1.add(6);
            al1.add(null); //non-synchronized
          al1.add(0, 5); // Add object at n index and all right side object shifted 
          al1.add(2, true);
          al1.set(3, 123.456); // It set object at n index
            System.out.println(al1);

            al2.add(15);
//            al2.add(15.64); It throw error al2 is Integer type ArrayList
            al2.add(6);
            al1.addAll(3, al2);
//            al1.addAll(al2);

            System.out.println(al1);
            System.out.println(al2);
//            System.out.println(al1.remove(5));
//            System.out.println(al1.remove("Keyur"));
            System.out.println(al1.contains(27));
            System.out.println(al1.containsAll(al2));
            System.out.println(al1.get(3));
            System.out.println(al1.equals(al2));
            System.out.println(al1.hashCode());
            System.out.println(al1.indexOf(6));
            System.out.println(al1.lastIndexOf(6));
            System.out.println(al1.size());
            System.out.println(al1.isEmpty());
            //System.out.println(al1.removeAll(al2));  //remove all elements of al2
//            System.out.println(al1.retainAll(al2)); // remove all elements of invoking collection except the specified collection.

            //al1.clear();

            // Fetching the elements by for loop
            System.out.println("By for loop");
            for(int i=0; i<al2.size(); i++){
                System.out.println(al2.get(i));
            }

            // Fetching the elements by forEach loop
            System.out.println("By forEach loop");
            for (Object element : al1) {  // al1 is mixed so Object type
                System.out.println(element);
            }

            // Fetching the elements by iterator
            System.out.println("By Iterator method of iterable interface");
            Iterator iterator = al1.iterator();
            while (iterator.hasNext()){
                System.out.println(iterator.next());
            }

            System.out.println("by arrow function forEach");
            al1.forEach(b-> System.out.println(b));
        }
}
