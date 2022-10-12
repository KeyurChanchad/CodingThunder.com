
// Objectives
// 1. Static Methods and Variables

void main() {

	var c1 = Circle();
	// c1.PI;     // 4 bytes
  // c1.color = "Blue";

	// var c2 = Circle();
//	c2.PI;     // 4 bytes
	// 8 bytes      // waste of extra 4 bytes

  c1.myNormalFunction();
	// c1.calculateArea();  // The static method and variable can't be accessed through an instance.

	Circle.PI;  // 4 bytes
	Circle.PI;  // No more memory will be allocated .

//	print(Circle.PI);           // Syntax to call Static Variable

	Circle.calculateArea();     // Syntax to call Static Method
  
}

class Circle {

	static const double PI = 3.14;
  static int maxRadius = 5;
  String color='';

	static void calculateArea() {
		print("Some code to calculate area of Circle");
    // print(PI);
//		myNormalFunction();     // Not allowed to call instance functions
//		this.color;             // You cannot use 'this' keyword and even cannot access Instance variables
	}

	void myNormalFunction() {
		calculateArea();
		this.color = "Red";
		print(PI);
		print(maxRadius);
	}
}
