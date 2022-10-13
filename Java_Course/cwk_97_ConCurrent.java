package com.company;

//Traditional   vs     ConCurrent Collection
//Traditional-> ArrayList, LinkedList, Vector, HashMap etc.

//problem
//1. They are not thread safe. (Data Inconsistency) Data concurrently(Parallel) read or write nahi horaha tha. ex. HashSet, HashMap
//2. Vector, Hashtable are synchronizedList() -thread safe. they are up to mark.
//3. If multiple thread perform read operation not an issue, but issue comes when thread perform write operation.

//fail safe vs fail fast

//Synchronized --> Thread safe --> but slow performance
//Non-Synchronized --> Not a Thread safe --> but fast performance

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;

//Concurrent Class
//    CopyOnWriteArrayList it is same as ArrayList but it fast and thread safe.
//    CopyOnWriteArraySet
//    ConcurrentHashMap
//etc..
public class cwk_97_ConCurrent extends Thread{
//    static Map<String, String> hm = new HashMap<String, String>();
static CopyOnWriteArrayList arrayList = new CopyOnWriteArrayList();
    public void run(){
        try {
            Thread.sleep(3000);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
//        hm.put("4", "nyx256e");
        arrayList.add(555);
        System.out.println(Thread.currentThread().getName());
    }
    public static void main(String[] args) {

//        ArrayList arrayList = new ArrayList();
//        arrayList.add(85);
//        arrayList.add(53);
//        arrayList.add(96);
//        arrayList.add(825);
// When you read data at a time you write data it gives error ConcurrentModificationException

//        Iterator i = arrayList.iterator();
//        while (i.hasNext()){
////            arrayList.add(63);
//            System.out.println(i.next());
//        }
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//        hm.put("1", "k263");
//        hm.put("2", "naya25e");
//        hm.put("3", "pqw422d");
        arrayList.add(36);
        arrayList.add(75);
        arrayList.add(85);
        cwk_97_ConCurrent thread = new cwk_97_ConCurrent();
        thread.setName("Mythread");
        thread.start();
        System.out.println("Main " + Thread.currentThread().getName());


//        Set es = hm.entrySet();
//        Iterator iterator = es.iterator();
//        while (iterator.hasNext()){
//            Map.Entry me = (Map.Entry) iterator.next();
//            System.out.println(me.getKey() + " : " + me.getValue());
//        }

        Iterator iterator = arrayList.iterator();
        while (iterator.hasNext()){
            System.out.println(iterator.next());
        }

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e){
            e.printStackTrace();
        }

//        System.out.println(hm);
        System.out.println(arrayList);
    }
}
