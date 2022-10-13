# 1.  Convert from JSON to Python:
import json

# some JSON:
x =  '{ "name":"Keyur", "age":21, "city":"New York"}'    # json is '{}' string file  dic {}

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
# print(type(y))
# print(y["city"])


#2.  Convert from Python to JSON:
import json

# a Python object (dict):
x = {
  "name": "keyur",
  "age": 21,
   "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
# print(type(y))
# print(y)

# You can convert Python objects of the following types, into JSON strings:
# dict, list, tuple, string, int, float ,True ,False, None

# Convert Python objects into JSON strings, and print the values:
import json

# print(json.dumps({"name": "Keyur", "age": 21}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print((json.dumps(None)))


# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
#
# Python	    JSON
# dict	        Object
# list	        Array
# tuple	        Array
# str	        String
# int	        Number
# float	        Number
# True	        true
# False	        false
# None	        null

# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "Keyur",
  "age": 21,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# print(type(x))
# print(json.dumps(x))

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:
# Use the indent parameter to define the numbers of indents:

# print(json.dumps(x, indent=4))

# You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
# Use the separators parameter to change the default separator:

# print( json.dumps(x, indent=4, separators=(" .", " = ")) )

# Order the Result
# The json.dumps() method has parameters to order the keys in the result:

# Example
# Use the sort_keys parameter to specify if the result should be sorted or not:

# print( json.dumps(x, indent=4, sort_keys=True) )


# json.load(): json.load() accepts file object, parses the JSON data,
# populates a Python dictionary with the data and returns it back to you.
# Syntax:
# json.load(file object)


# Python program to read json file

# import json
# Opening JSON file
# f = open('example_2.json',)

# returns JSON object as a dictionary
# data = json.load(f)

# Iterating through the json list
# for i in data['quiz']['maths']['q1']['options']:
# 	print(i)

# Closing file
# f.close()


# Python program to read json file

# import json
# JSON string
a = '{"name": "Bob", "languages": "English"}'

# deserializes into dict and returns dict.
y = json.loads(a)

print("JSON string = ", y)
print()



# JSON file
f = open ('example_2.json', "r")

# Reading from file
data = json.loads(f.read())

# Iterating through the json list
for i in data['quiz']['maths']:
	print(i)

# Closing file
f.close()

# indent :
# It improves the readability of the json file.
# The possible values that can be passed to this parameter are simply double quotes(""),
# any integer values. Simple double quotes makes every key-value pair appear in new line.

# json dumps()
data2 = {
    "channel_name": "CodeWithKeyur",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jsonvar = json.dumps(data2)
print(jsonvar)

# json.dump()
# json module in Python module provides a method called dump() which converts the Python objects into appropriate json objects.
# It is a slight variant of dumps() method.

import json

# python object(dictionary) to be dumped
dict1 ={
	"emp1": {
		"name": "Lisa",
		"designation": "programmer",
		"age": "34",
		"salary": "54000"
	},
	"emp2": {
		"name": "Elis",
		"designation": "Trainee",
		"age": "24",
		"salary": "40000"
	},
}

# the json file where the output must be stored
out_file = open("myjsonfile.json", "w")

json.dump(dict1, out_file, indent = 6)
# json.dump(dict1,out_file,sort_keys=True)

out_file.close()
