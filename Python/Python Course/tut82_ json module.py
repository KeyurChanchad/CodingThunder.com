"""
JSON stands for JavaScript Object Notation.
JSON is a data-interchange format, derived from JavaScript. It is mostly used for storing or transferring data.
So, if we want our program to interact with the internet, we must be familiar with this module, even only to send or receive data through the internet.
It is one of Python's most important modules because, however small level of our program is if we want it to interact only a bit through the internet,
the Json module must be imported first. A JSON is an unordered collection of key and value pairs similar to a python dictionary.
The following are some important points about JSON.

Keys are unique strings that cannot be null.
Values can be anything from a String, Number, Tuple, Boolean, list, or null.
A JSON is represented by a string which is enclosed within curly braces { } with key-value pairs which are separated by a colon ( : ), and pairs separated by a comma(, ).

{"name": "harry", "salary": 9000, "language": "Python"}

If we convert a JSON string to a Python, the resultant will be a dictionary. The conversion is also known as parsing,
and that is the keyword we use professionally for the conversion.
We can either convert from JSON to Python or from Python to JSON by using json.loads() or json.dumps() methods. Methods:

load(): This method is used to load data from a JSON file into a python dictionary.
Loads( ): This method is used to load data from a JSON variable into a python dictionary.
dump():This method is used to load data from the python dictionary to the JSON file.
dumps(): This method is used to load data from the python dictionary to the JSON variable.

Ex.
    import json
    a ={"name":"harry","salary":9000,"language":"Python"}
    # conversion to JSON done by dumps() function
    b = json.dumps(a)
    print(b) # printing the output

"""


import json

data = '{"var1":"keyur", "var2":56}'
print(data)

parsed = json.loads(data)
# print(type(parsed))
print(parsed['var1'])

#Task 1 - json.load?     json file to python dictionary


data2 = {
    "channel_name": "CodeWithKeyur",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jsonvar = json.dumps(data2)
print(jsonvar)

# Task 2 = what is sort_keys parameter in dumps    it is sorted



import  json

print( json.dumps({'4': 5 , '6': 7}, sort_keys=True, indent= 4 ) )




