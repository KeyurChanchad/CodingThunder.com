package com.company;
import java.util.Comparator;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;


//SortedSet is the alternate of Set interface that provides a total ordering on its elements. The elements of the SortedSet are arranged in the increasing (ascending) order. The SortedSet provides the additional methods that inhibit the natural ordering of the elements.

//Java TreeSet class implements the Set interface that uses a tree for storage. Like HashSet, TreeSet also contains unique elements. However, the access and retrieval time of TreeSet is quite fast. The elements in TreeSet stored in ascending order.

class Emp {//implements Comparable{
    int age;
    String name, city;

    Emp(int age, String name, String city) {
        this.age = age;
        this.name = name;
        this.city = city;
    }

    public String toString(){
        System.out.println();
        return name + " " + age + " " + city;
    }

    //This sort by age only
//    @Override
//    public int compareTo(Object obj) {
//        Emp e = (Emp) obj;
//        if (this.age > e.age){
//            return 1;
//        }
//        else if(this.age < e.age){
//            return -1;
//        }
//        else
//        return 0;
//    }

    public void show(){
        System.out.println("Name " + this.name + " Age " + age + " city " +city);
    }
}
public class cwk_95_treeSet {
    public static void main(String[] args) {
//        TreeSet follow tree rules of data structure. TreeSet add() only contains comparable type object. Every Wrapper class implements java.lang.Comparable.
//        It sorts values by compareTo method. When add() method invoke it automatically invoke compareTo() of its Wrapper Class(Integer, String, Float etc). When we add multi type values in TreeSet it confuse which compareTo() call. Basically compareTo() is responsible to sort the element.


        TreeSet ts = new TreeSet();
        // sort by Integer class compareTo method
//        ts.add(152);
//        ts.add(63);
//        ts.add(96);

        // sort by String class compareTo method
        ts.add("Priya");
        ts.add("Anu");
        ts.add("Angelika");

        // sort by Float class compareTo method
//        ts.add(23.12);
//        ts.add(56.2);
//        ts.add(78.52);

//        System.out.println(ts);


        Emp e1 = new Emp(21, "Keyur", "Los Angeles");
        Emp e2 = new Emp(23, "Ankit", "Swidan");
        Emp e3 = new Emp(25, "Vishal", "Singapore");
        Emp e4 = new Emp(26, "Sahil", "Lucknow");
        Emp e5 = new Emp(21, "Chanchad", "India");// it ignore in age comparison due to duplicate.

//        System.out.println("Emp Object " + e1);
//        Set<Emp> s = new TreeSet<Emp>();

        Comparator c = new cwk_95_ByNameComparing();
//        Comparator c = new cwk_95_ByCityComparing();
//        Comparator c = new cwk_95_ByAgeComparing();
        Set<Emp> s = new TreeSet<Emp>(c);

        //If we want to add Emp type object in TreeSet than it must be comparable type Object. so Emp class implements Comparable and must override compareTo().
        s.add(e1);
        s.add(e2);
        s.add(e3);
        s.add(e4);
        s.add(e5);

//        System.out.println(s);
        Iterator<Emp> iterator = s.iterator();
        while (iterator.hasNext()){
            Emp emp = (Emp) iterator.next();
            emp.show();
        }

    }
}