package com.company;
// java docs 14 use
import java.util.HashSet;

public class cwk_95_hashing_set {

        public static void main(String[] args) {
            HashSet<Integer> myHashSet = new HashSet<>(6, 0.5f);
            myHashSet.add(6);
            myHashSet.add(28);
            myHashSet.add(3);
            myHashSet.add(11);
            myHashSet.add(11);  // it ignore duplicate value

            System.out.println(myHashSet);
        }
}
