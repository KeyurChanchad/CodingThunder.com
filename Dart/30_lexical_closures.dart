

// Objective
// 1. Closures (Local and Global)


void main() {

	// Definition 1:
	// A closure is a function that has access to the parent scope, even after the scope has closed.

	String message = "Dart is good";  //This is global variable

	Function showMessage = () {
		message = "Dart is awesome";   //This is local variable
		print(message);
	};

	showMessage();


	// Definition 2:
	// A closure is a function object that has access to variables in its lexical scope,
	// even when the function is used outside of its original scope.

	Function talk = () {

		String msg = "Hi";  //global variable

		Function say = () {
			msg = "Hello";  //Local variable
			print(msg);
		};

		return say;
	};

	Function speak = talk();

	speak();        // talk()       // say()        //  print(msg)      // "Hello"
}
