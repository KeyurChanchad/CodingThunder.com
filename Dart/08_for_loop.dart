
void main() {

	// FOR Loop

	// WAP to find the even numbers between 1 to 10

	for (int i = 1; i <= 10; i++) {

		if ( i % 2 == 0) {
			print(i);
		}
	}


	// for ..in loop
	List planetList = ["Mercury", "Venus", "Earth", "Mars"];
  List groceries = ["Harpic", 33, 36.55, true, ["Burger", 5]];

	for (String planet in planetList) {
		print(planet);
	}
    
  for (var grocery in groceries ){
    print(grocery);
  }

  
}
