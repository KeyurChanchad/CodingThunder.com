package com.company;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Properties;

public class cwk_144_Property {
    public static void main(String[] args) {
        try{
            String file = System.getProperty("user.dir");
//            System.out.println(file);
            file = "C:\\Users\\Lenovo\\IdeaProjects\\FirstJavaProgramCWK\\src\\com\\company\\mytext.properties";

            Properties p = new Properties();
            FileInputStream fs = new FileInputStream(file);
            p.load(fs);
            String value = p.getProperty("mytext");
            System.out.println(value);

            p.setProperty("url", "localhost");
            p.setProperty("port", "5500");
            p.setProperty("protocol", "https://");

            FileOutputStream fo  = new FileOutputStream("abcd.txt");
            p.store(fo, "by keyur");
        }
        catch (IOException e){
            e.printStackTrace();
        }


    }
}
