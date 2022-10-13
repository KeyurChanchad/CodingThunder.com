package com.company;

import java.util.*;

public class CWK_90_Collection {
    public static void main(String[] args) {
        List arraylist = new ArrayList();

        arraylist.add(15);
        arraylist.add(96);
        arraylist.add(75);
        arraylist.add(34);
        arraylist.add(96);

        System.out.println(arraylist);

        //It reverse any Collection object
        Collections.reverse(arraylist);//it change original Collection
        System.out.println(arraylist);

        //It sort any Collection object
        Collections.sort(arraylist);//it change original Collection
        System.out.println(arraylist);

        //It find min and max in Collection
        System.out.println(Collections.max(arraylist));
        System.out.println(Collections.min(arraylist));

        //It change in unmodified Collection.
        List l = Collections.unmodifiableList(arraylist);

        Iterator itr = l.iterator();
        while (itr.hasNext()){
            System.out.println(itr.next());
        }

//        l.add(62); //gives error due to unmodified
    }
}
