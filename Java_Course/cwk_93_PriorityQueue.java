package com.company;
import java.util.Iterator;
import java.util.Queue;
import java.util.PriorityQueue;

//Queue interface maintains the first-in-first-out order. It can be defined as an ordered list that is used to hold the elements which are about to be processed. There are various classes like PriorityQueue, Deque, and ArrayDeque which implements the Queue interface.

//Queue<String> q1 = new PriorityQueue();
//Queue<String> q2 = new ArrayDeque();

//The PriorityQueue class implements the Queue interface. It holds the elements or objects which are to be processed by their priorities. PriorityQueue doesn't allow null values to be stored in the queue.

public class cwk_93_PriorityQueue {
    public static void main(String[] args) {
        PriorityQueue<String> pq = new PriorityQueue<>();

        pq.add("keyur");
        pq.add("Ankit");
        pq.add("Vishal");
//        pq.add(null);

        System.out.println(pq);
        System.out.println("head:"+pq.element());
        System.out.println("head:"+pq.peek());
        System.out.println(pq.poll());

        System.out.println(pq.size());
        System.out.println("iterating the queue elements:");
        Iterator itr=pq.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
        pq.remove(); // it delete first element
        pq.poll(); // it delete last element
        System.out.println("after removing two elements:");
        Iterator<String> itr2=pq.iterator();
        while(itr2.hasNext()){
            System.out.println(itr2.next());
        }
    }
}
