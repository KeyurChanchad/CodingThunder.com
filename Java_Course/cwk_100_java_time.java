package com.company;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class cwk_100_java_time {
        public static void main(String[] args) {
            LocalDate d = LocalDate.now();
          //  LocalDate dt = new LocalDate(2021, 3 , 24);
            System.out.println(d);

            LocalTime t = LocalTime.now();
            System.out.println(t);

            LocalDateTime dt = LocalDateTime.now();
            System.out.println(dt);
        }
}
