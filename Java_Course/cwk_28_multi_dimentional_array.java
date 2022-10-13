package com.company;

public class cwk_28_multi_dimentional_array {

        public static void main(String[] args) {
            int [] marks; // A 1-D Array
            int [][] flats; // A 2-D Array  <-------Declaration
            flats = new int [2][3];        // <------- 2 rows and 3 column
            flats[0][0] = 101;              // --------initialisation
            flats[0][1] = 102;
            flats[0][2] = 103;
            flats[1][0] = 201;
            flats[1][1] = 202;
            flats[1][2] = 203;

            // Displaying the 2-D Array (for loop)
            System.out.println("Printing a 2-D array using for loop");
            for(int i=0;i<flats.length;i++){
                for(int j=0;j<flats[i].length;j++) {
                    System.out.print(flats[i][j]);
                    System.out.print(" ");
                }
                System.out.println("");
            }

        }
    }
