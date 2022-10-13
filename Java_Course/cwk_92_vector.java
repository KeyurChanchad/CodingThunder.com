package com.company;
import java.util.Iterator;
import java.util.Vector;

//Vector uses a dynamic array to store the data elements. It is similar to ArrayList. However, It is synchronized and contains many methods that are not the part of Collection framework.
public class cwk_92_vector {
    public static void main(String[] args) {
        //initial capacity 10 and increment by 50% of its size means nextTime 15
        Vector<String> v=new Vector<String>();// only contains string values

        Vector vc1 = new Vector(7);
        Vector<Integer> vc2 = new Vector<Integer>(7, 3); //increment by 3 when object beyond capacity
        Vector<Integer> vc3 = new Vector<Integer>(vc2);

        v.add("Neha");
        v.add("Shreya");
        v.add("Man");
        v.add("Shailaja");
        v.add(1, "Mouny Roy");

        vc1.add(15);
        vc1.add(15);
        vc1.addElement(53.25);
        v.addAll(vc1);


        System.out.println(v.capacity());
        System.out.println(v.elementAt(3));
        System.out.println(v.equals(vc1));
        System.out.println(v.firstElement());
        System.out.println(v.removeElement(15));
        System.out.println(v.toArray());
//        System.out.println(v.retainAll(vc1));

//        Iterator<String> itr=v.iterator();
        Iterator itr=v.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
    }
}
