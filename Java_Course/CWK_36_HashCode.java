package com.company;

public class CWK_36_HashCode {
    public static void main(String[] args) {
        CWK_36_HashCode obj = new CWK_36_HashCode();

        System.out.println(obj);
//        System.out.println(obj.getClass());
        String class_name = obj.getClass().getName();
        int hashcode = obj.hashCode();
        String hash_string = Integer.toHexString(obj.hashCode());
//        System.out.println(hash_string);

//        String ref_code = class_name+"@"+hash_string;
//        System.out.println(ref_code);

        System.out.println(obj.getClass().getName()+"@"+Integer.toHexString(obj.hashCode()));
    }
}
