package com.company;

import java.util.*;

// 1. ordering not important
// 2. key must be unique

public class cwk_96_HashMap {
    public static void main(String[] args) {
        //This is loosely typed couple where object of implementing class store in reference class.
        //There is only one difference in HashMap and LinkedHashMap. In HashMap ordering not matter but LinkedHashMap show data in ordering form.
        Map<String, String> hm = new HashMap<String, String>();
//        Map<String, String> hm = new LinkedHashMap<String, String>();

        hm.put("101", "Keyur");
        hm.put("215", "Ram");
        hm.put("345", "Krishan");
        hm.put("670", "Surya");
        hm.put("101", "Narayan");
        hm.put("555", "Rolex");

        System.out.println(hm);
//        System.out.println(hm.size());
//        System.out.println(hm.isEmpty());
//        System.out.println(hm.containsKey("215"));
//        System.out.println(hm.containsValue("Shiva"));
//        System.out.println(hm.get("215"));
//        System.out.println(hm.remove("555")); // if removed than return value else null
//        System.out.println(hm.remove("555", "Rolex")); //  if removed than return true else false
//        System.out.println(hm.replace("670", "Suryabhai"));
//        System.out.println(hm);

        System.out.println("~~~~~~~ Keys ~~~~~~~");
        Set ks = hm.keySet();
        Iterator i = ks.iterator();
        while (i.hasNext()){
            System.out.println(i.next());
        }

        System.out.println("~~~~~~~ Values ~~~~~~~");
        Collection vc = hm.values();
        Iterator j = vc.iterator();
        while (j.hasNext()){
            System.out.println(j.next());
        }

        System.out.println("~~~~~~~ Key and Value ~~~~~~~");
        Set es = hm.entrySet();
        Iterator k = es.iterator();
        while (k.hasNext()){
            System.out.println(k.next());
        }

        System.out.println("~~~~~~~ Key and Value ~~~~~~~");
        Set kv = hm.entrySet();
        Iterator iterator = kv.iterator();
        while (iterator.hasNext()){
            Map.Entry me = (Map.Entry) iterator.next();
            System.out.println("key " + me.getKey() + " and value " + me.getValue());
        }
    }
}
