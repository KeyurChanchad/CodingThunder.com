package com.company;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;

class EmpUser{
    int id;
    String name;
    EmpUser(int id, String name){
        this.id = id;
        this.name = name;
    }
    public String toString(){
        return id + " " + name;
    }
}
public class cwk_97_Collection_Lambda {
    public static void main(String[] args) {
        // Collections.sort() not sort User define class
        EmpUser emp1 = new EmpUser(4, "Johny");
        EmpUser emp2 = new EmpUser(2, "Deep");
        EmpUser emp3 = new EmpUser(3, "Jack");
        EmpUser emp4 = new EmpUser(1, "Sparrow");

        List<EmpUser> arraylist = new ArrayList<EmpUser>();
        arraylist.add(emp1);
        arraylist.add(emp2);
        arraylist.add(emp3);
        arraylist.add(emp4);

        System.out.println(arraylist);

        //We can sort by Comparable and Comparator also.
        Collections.sort(arraylist, (a, b)->{
//            return a.name.compareTo(b.name);
             if (a.id > b.id)
                 return 1;
             else
                 return -1;
        });

        for (EmpUser obj : arraylist){
            System.out.println(obj);
        }

        //If we want to apply some condition on object
        Stream<EmpUser> f_data = arraylist.stream().filter(obj->obj.id > 2);
        f_data.forEach(obj-> System.out.println(obj));
    }
}
