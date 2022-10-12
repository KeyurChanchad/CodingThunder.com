
void main() {

	// Using Labels
	myOuterLoop: for (int i = 1; i <= 4; i++) {

	// Nested FOR Loop
		innerLoop: for (int j = 1; j <= 4; j++) {

			if (i == 2 && j == 2) {
	// BREAK keyword
				break myOuterLoop;
			}
			print("$i $j");
		}
	}
}
