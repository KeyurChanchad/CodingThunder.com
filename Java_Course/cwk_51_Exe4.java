package com.company;
class library {
    String [] book;
    int noofbooks = 0 ;

    public library() {
        this.book = new String[20];
    }

    public int getNoofbooks() {
        return noofbooks;
    }

    public void setNoofbooks(int noofbooks) {
        this.noofbooks = noofbooks;
    }

    void addBook(String book){
        this.book[noofbooks] = book;
        System.out.println(book + " has been added successfully..");
        noofbooks++;
    }
    void returnBook(String retbook){
            this.book[noofbooks] = retbook;
        System.out.println("The book has returned.");
            noofbooks++;
    }
    void showAvailableBook(){
        for (String book : this.book) {
            if (book == null) {
                break;
            }
            System.out.println(" * " + book);
        }
    }
}
public class cwk_51_Exe4 {

        public static void main(String[] args) {
            // You have to implement a library using Java Class "Library"
            // Methods: addBook, issueBook, returnBook, showAvailableBooks
            // Properties: Array to store the available books,
            // Array to store the issued books

            library l = new library();
            l.addBook("C# Window Programing");
            l.addBook("C++");
            l.addBook("Core JAVA");
            l.showAvailableBook();
            l.returnBook("C++");
            l.returnBook("C# Window Programing");
            l.showAvailableBook();


        }
    }
