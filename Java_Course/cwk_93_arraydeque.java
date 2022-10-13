package com.company;

import java.util.ArrayDeque;
import java.util.Deque;
//Deque interface extends the Queue interface. In Deque, we can remove and add the elements from both the side. Deque stands for a double-ended queue which enables us to perform the operations at both the ends.

//ArrayDeque class implements the Deque interface. It facilitates us to use the Deque. Unlike queue, we can add or delete the elements from both the ends.

// ArrayDeque is faster than ArrayList and Stack and has no capacity restrictions.

public class cwk_93_arraydeque {

        public static void main(String[] args) {
//            Deque d = new ArrayDeque(); this is recommend
            ArrayDeque<String> ad1 = new ArrayDeque<>();
            ad1.addFirst("Keyur");
            ad1.add("Ankit");
            ad1.add("Vishal");
            ad1.addLast("Sahil");
            System.out.println(ad1.getFirst());
            System.out.println(ad1.getLast());
            System.out.println(ad1.pop());
            System.out.println(ad1.peek());
            System.out.println(ad1.pollLast());
//            System.out.println(ad1.removeFirst());

            //Traversing elements
            for (String str : ad1) {
                System.out.println(str);
            }
        }
}
