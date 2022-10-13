package com.company;

import java.util.Date;

public class cwk_97_date_class {

        public static void main(String[] args) {
            // In java time start 1 jan 1970
            System.out.println(System.currentTimeMillis());
            System.out.println("Total years from 1970 " + System.currentTimeMillis()/1000/3600/24/365);

            // Millisecond is store in long
//        System.out.println(Long.MAX_VALUE);
//        System.out.println(System.currentTimeMillis());
            Date d = new Date();
            System.out.println(d);
            System.out.println(d.getTime());
            System.out.println(d.getDate());
            System.out.println(d.getSeconds());
            System.out.println(d.getYear());
           // System.out.println(d.after(2001));  java doc14
        }

}
