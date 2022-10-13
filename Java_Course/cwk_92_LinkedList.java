package com.company;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
//LinkedList implements the Collection interface. It uses a doubly linked list internally to store the elements. It can store the duplicate elements. It maintains the insertion order and is not synchronized. In LinkedList, the manipulation is fast because no shifting is required.

//1. store duplicate value
//2. insertion order
//3. not shifting
public class cwk_92_LinkedList {

        public static void main(String[] args) {
            // Use java 14 documentation
            LinkedList<Integer> l1 = new LinkedList<>(); //initialCapacity 10
            LinkedList l2 = new LinkedList(l1);


            l2.add(15);
            l2.add("Keyur");
            l2.add(45.965);

            l1.add(6);
            l1.add(7);
            l1.add(4);
            l1.add(6);
//            l1.add(0, 5); //Add with index
            l1.addFirst(50); // Add at first
            l1.addLast(555); // Add at last
            l1.set(2, 99);
//            l1.addAll(0, l2);
            l1.addAll(l2);
//            l1.remove(7);
//            l1.removeFirst();
//            l1.removeLast();

            //It contains all method of collection interface
            System.out.println(l1);
            System.out.println(l1.contains(27));
            System.out.println(l1.indexOf(6));
            System.out.println(l1.getFirst());
            System.out.println(l1.getLast());
            System.out.println(l1.lastIndexOf(6));
            System.out.println(l1.peek()); //Retrieves, but does not remove, the head (first element) of this list.
            System.out.println(l1.peekFirst()); //Retrieves, but does not remove, the first element of this list, or returns null if this list is empty.
            System.out.println(l1.peekLast()); //Retrieves, but does not remove, the last element of this list, or returns null if this list is empty.
            System.out.println(l1.pop()); // removes and returns the first element of this list. This method equals to removeFirst().
            System.out.println(l1.poll()); //Retrieves and removes the head (first element) of this list.
            System.out.println(l1.pollFirst());//Retrieves and removes the first element of this list, or returns null if this list is empty
            System.out.println(l1.pollLast());//Retrieves and removes the last element of this list, or returns null if this list is empty
            System.out.println(l1);
            //l1.clear();

            //In iterator method it goes only in forward direction.
            System.out.println("iterator method");
            Iterator itr = l1.iterator();
            while (itr.hasNext()){
                System.out.println(itr.next());
            }

            //List iterator traverse in both direction. In list iterator by default pointer initialize at -1 so by forward it came at end of collection.
            System.out.println("List iterator forward direction");
            ListIterator fitr = l1.listIterator();
            while (fitr.hasNext()){
                System.out.println(fitr.next());
            }

            //It came back from end to start
            System.out.println("List iterator backward direction");
            ListIterator bitr = l1.listIterator();
            while (bitr.hasPrevious()){
                System.out.println(bitr.previous());
            }
        }
}
