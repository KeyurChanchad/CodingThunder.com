
// 1. Required Parameters
// 2. Optional Positional Parameters

void main() {

	printCities("New York", "Washington", "Los Angeles");
	print("");

	printCountries("USA");  // You can skip the Optional Positional Parameters

}

// Required Parameters
void printCities(String city1, String city2, String city3) {

	print("Name 1 is $city1");
	print("Name 2 is $city2");
	print("Name 3 is $city3");
}

// Optional Positional Parameters
void printCountries(String name1, [var name2, var name3]) {  //String cann't have a value of null

	print("Name 1 is $name1");
	print("Name 2 is $name2");
	print("Name 3 is $name3");
}
