
// Objectives
// 1. Abstract Method
// 2. Abstract Class

void main() {

	// var shape = Shape();        // Error. Cannot instantiate Abstract Class

	var rectangle = Rectangle();
	rectangle.draw();

	var circle = Circle();
	circle.draw();
}

abstract class Shape {

	// Define your Instance variable if needed
	int x = 0;
	int y = 0;

	void draw();        // Abstract Method

	void myNormalFunction() {
		print("This is normal function in abstract class");
	}
}


class Rectangle extends Shape {

// When you extends abstract class then must be override all abstract method
	void draw() {
		print("Drawing Rectangle.....");
	}

  // void myNormalFunction(){
  //   //code
  // }
}

class Circle extends Shape {

	void draw() {
		print("Drawing Circle.....");
	}
}
