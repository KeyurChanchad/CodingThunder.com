package com.company;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Objects;
import java.util.Set;

//Java HashSet class is used to create a collection that uses a hash table for storage. It inherits the AbstractSet class and implements Set interface.
//HashSet stores the elements by using a mechanism called hashing.
//HashSet contains unique elements only.
//HashSet allows null value.
//HashSet class is non synchronized.
//HashSet doesn't maintain the insertion order. Here, elements are inserted on the basis of their hashcode.
//HashSet is the best approach for search operations.
//The initial default capacity of HashSet is 16, and the load factor is 0.75.

//Ones we create object of the HashSet class internally it create Hashtable in memory. Basically it is HashMap class instance. Hashtable is ArrayList of LinkedList where every LinkedList is bucket and by default it is 16 sized. backet-0 to backet-15

//When we invoke add(OBJECT) of HashSet it internally create HashMap class object. OBJECT put in Hashtable by object of HashMap in add() of HashSet.

//Indexing in Hashtable by OBJECT.hashcode / size of bucket.


class Myemp{
    int id;
    String name, address;

    public Myemp(int id, String name, String address) {
        this.id = id;
        this.name = name;
        this.address = address;
    }

    @Override
    public int hashCode() {
        return this.id;
    }

    @Override
    public boolean equals(Object obj){
        Myemp emp = (Myemp) obj;
        if (this.id == emp.id)
                return true;
        else
            return false;
    }
    public String toString(){
        return this.id + " " + this.name + " " + this.address;
    }

    public void show(){
        System.out.println(this.id + " " + this.name + " " + this.address);
    }
}
public class cwk_94_HashSet {
    public static void main(String[] args) {
//        Set<String> set = new HashSet<String>(); // CAPACITY 16 and LoadFactor 0.75
//        set.add("Keyur");
//        set.add("Nayan");
//        set.add("Keyur");
//        set.add("Pritam");

//        HashSet hs1 = new HashSet(5);//staring capacity of 5 object and increment with 75% due to load factor. By default load factor is 0.75.

//        HashSet HS = new HashSet(hs1);

//        hs1.add(852);
//        hs1.add(174);
//        hs1.add(174);// it ignore duplicate value
//        hs1.add(425);
//        hs1.add(245);
//        hs1.add(876);
//        hs1.add(174);// it ignore duplicate value
//        System.out.println(hs1); //ordering not important

//Traversing elements
//        Iterator<String> itr = set.iterator();
//        while (itr.hasNext()) {
//            System.out.println(itr.next());
//        }

        HashSet<Myemp> ushs = new HashSet<Myemp>(7, 0.4f);// initial capacity of 7 object and increment with 40% that is depend on load factor.


        Myemp e1 = new Myemp(524, "Keyur", "Indraprastha");
        Myemp e2 = new Myemp(235, "Ankit", "Gandhar");
        Myemp e3 = new Myemp(142, "Nayan", "Mithila");
        Myemp e4 = new Myemp(463, "Vishal", "Lanka");
        Myemp e5 = new Myemp(524, "Keyur", "Indraprastha");

        //Normally hashCode of every objects are different So,IN USER DEFINE CLASS HashSet ALLOW DUPLICATE VALUE but by overriding hashCode() and equals() we fix it.
        System.out.println(e1.hashCode());
        System.out.println(e2.hashCode());
        System.out.println(e3.hashCode());
        System.out.println(e4.hashCode());
        System.out.println(e5.hashCode());

        ushs.add(e1);
        ushs.add(e2);
        ushs.add(e3);
        ushs.add(e4);
        ushs.add(e5);

        Iterator<Myemp> iterator = ushs.iterator();
        while (iterator.hasNext()){
            Myemp emp = (Myemp) iterator.next();
            emp.show();
        }

    }
}
