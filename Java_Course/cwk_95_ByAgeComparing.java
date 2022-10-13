package com.company;

import java.util.Comparator;
import java.lang.Comparable;

public class cwk_95_ByAgeComparing implements Comparator {

    @Override
    public int compare(Object o1, Object o2) {
        Emp obj1 = (Emp) o1;
        Emp obj2 = (Emp) o2;
        if (obj1.age > obj1.age){
            return 1;
        }
        else if(obj1.age < obj2.age){
            return -1;
        }
        else
            return 0;
    }
}
