package com.company;

public class CWK_14_String_Method {
    public static void main(String[] args) {
//                STRING HANDING
                 String name = "Keyur", sirname = "Chanchad";
//                 System.out.println(name);

//                int value = name.length();
//                System.out.println(value);

//                String lstring = name.toLowerCase();  //in camelCase
//                System.out.println(lstring);

//                String ustring = name.toUpperCase();
//                System.out.println(ustring);
//
                String concatStr = name.concat(sirname);
//                System.out.println(concatStr);

//                String nonTrimmedString = "     Keyur     ";
                //System.out.println(nonTrimmedString);

                //String trimmedString = nonTrimmedString.trim();
                //System.out.println(trimmedString);

                //substring(start index, end index) takes 1 or 2 arguments if 1 agrument given that end with string length.
//                System.out.println(name.substring(1));
//                if 2 argument given then 2 is ending index but not include
//                System.out.println(name.substring(1, 3));

//                String greet = "Hey, Keyur How are you? Keyur nice to meet you, Keyur by...";
//                String str_arr[] = greet.split("Keyur", 2);
//                for (String s :str_arr) {
//                    System.out.println(s);
//                }


//                System.out.println(name.replace('r', 'p'));
//                System.out.println(name.replace( "r", "ier"));

//                System.out.println(name.startsWith("Key"));
//                System.out.println(name.endsWith("dd"));

                System.out.println(name.charAt(4));

                String modifiedName = "Keyuryuryurr";
                System.out.println(modifiedName.indexOf("yur")); //return index number
                System.out.println(modifiedName.indexOf("yur", 5)); //start with 5 index with first occurence
                System.out.println(modifiedName.lastIndexOf("yur", 7)); //

                System.out.println(name.equals("keyur"));
                System.out.println(name.equalsIgnoreCase("kEyUr"));

//                System.out.println("I am escape sequence\t\"double quote");  }

    }
}
