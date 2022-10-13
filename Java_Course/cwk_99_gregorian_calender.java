package com.company;

import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.TimeZone;

public class cwk_99_gregorian_calender {

        public static void main(String[] args) {
            Calendar c = Calendar.getInstance();
            System.out.println(c.getTime());
            System.out.println(c.get(Calendar.DATE));
            System.out.println(c.get(Calendar.SECOND));
            System.out.println(c.get(Calendar.HOUR));
            System.out.println(c.get(Calendar.HOUR_OF_DAY) + ":" +
                    c.get(Calendar.MINUTE) + ":" + c.get(Calendar.SECOND));

            GregorianCalendar cal = new GregorianCalendar();
            System.out.println(cal.isLeapYear(2018));
            System.out.println( cal.get(Calendar.DATE) );
            System.out.println(cal.getCalendarType() );
            System.out.println(TimeZone.getAvailableIDs()[0]);
            System.out.println(TimeZone.getAvailableIDs()[123]);
            System.out.println(TimeZone.getAvailableIDs()[210]);
        }

}
