package com.company;

class MyEmployee{
    private int id;
    private String name;

    public String getName(){
        return name;
    }
    public void setName(String n){
        this.name = n;
    }
    public void setId(int i){
        this.id = i;
    }
    public int getId(){
        return id;
    }
}
public class cwk_40_ch9 {

        public static void main(String[] args) {
//   Modifier             class      Packges      SubCalss     World
//    public              Yes         Yes             Yes         Yes
//    protected           Yes         Yes             Yes         No
//    private             Yes         No              No          No
//    no_modifer(default)  Yes        Yes             No          No
            MyEmployee keyur = new MyEmployee();
            // keyur.id = 45;
            // keyur.name = "CodeWithkeyur"; --> Throws an error due to private access modifier
            keyur.setName("CodingThunder.com");
            System.out.println(keyur.getName());
            keyur.setId(234);
            System.out.println(keyur.getId());
        }
    }
