package com.company;

import java.util.Comparator;

public class cwk_95_ByNameComparing implements Comparator {
    @Override
    public int compare(Object o1, Object o2) {
        Emp obj1 = (Emp) o1;
        Emp obj2 = (Emp) o2;
        return obj1.name.compareTo(obj2.name);
    }
}
