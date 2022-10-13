package com.company;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.Set;

//Set Interface in Java is present in Collection interface. It represents the unordered set of elements which doesn't allow us to store the duplicate items. We can store at most one null value in Set. Set is implemented by HashSet, LinkedHashSet, and TreeSet.
//        Set<data-type> s1 = new HashSet<data-type>();
//        Set<data-type> s2 = new LinkedHashSet<data-type>();
//        Set<data-type> s3 = new TreeSet<data-type>();
//1. unordered
//2. unique value

//LinkedHashSet class represents the LinkedList implementation of Set Interface. It extends the HashSet class and implements Set interface. Like HashSet, It also contains unique elements. It maintains the insertion order and permits null elements.

public class
cwk_94_LinkedHashSet {
    public static void main(String[] args) {
        LinkedHashSet<String> set=new LinkedHashSet<String>();
        set.add("Keyur");
        set.add("Ankit");
        set.add("Vishal");
        set.add("Sahil");

        Iterator<String> itr=set.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
    }
}
