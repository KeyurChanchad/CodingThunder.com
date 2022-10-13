# Create a dictionary and take input from the user and return the meaning of the word from  the dictionary

Dict = {"Array":"array is a collection of homogeneous data type",
        "Set":"set is a collection of predefine word",
        "Akbar":"The king Jalaluddin Muhammad Akbar was great king in mughal saltanat"}

str = input("Enter a word of Dict\n")
word = str.capitalize()
print(Dict[word])