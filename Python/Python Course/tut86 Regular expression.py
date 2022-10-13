"""
Regular expressions are used to perform search or validation related tasks in Python. To work with regular expressions, we have to import a built-in module in python called ‘re’.
import re

The module defines several functions and constants to work with RegEx. The “re” module is composed of five functions known as:

findall:      It finds all search for matches and print resultant in the form of a list.
search:       It works the same as a findall, but the resultant is a matched object, if any found.
split:        The split function splits the string from every matched into two new strings.
sub:          The sub-function works exactly like a replace function in notepad or MS Word, it replaces the original word,
                with a word of our choice.
finditer:     The finditer yields an iterator as a resultant with all the objects that match the one we sent it)
              finditer supports more attributes than any other function defined above. It also provides more details
              related to the matched object.
              So, most of the examples we are going to see next will contain a finditer function in them.

Meta Characters
[]          A set of characters
\           Signals a special sequence (can also be used to escape special characters)
.           Any character (except newline character) Zero or one
^           Starts with
$           Ends with
*           Zero or more occurrences
+           One or more occurrences
{}          Exactly the specified number of occurrences
|           Either or
()          Capture and group

Special Sequences
\A          Returns a match if the specified characters are at the beginning of the string
\b          Returns a match where the specified characters are at the beginning or at the end of a word i.e: r"ain\b"
\B          Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d          Returns a match where the string contains digits (numbers from 0-9)
\D          Returns a match where the string DOES NOT contain digits
\s          Returns a match where the string contains a white space character
\S          Returns a match where the string DOES NOT contain a white space character
\w          Returns a match where the string contains any word characters
            (characters from a to Z, digits from 0-9, and the underscore _ character)
\W          Returns a match where the string DOES NOT contain any word characters
\Z          Returns a match if the specified characters are at the end of the string
"""


import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# findall, search, split, sub, finditer
# patt = re.compile(r'fass')   # return match object
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iii$')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){2}')
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'Fax\b')  # strating or ending of word
# patt = re.compile(r'27\b')
patt = re.compile(r'\d{5}-\d{4}')
# Task
# Given a string with a lot of indian phone numbers starting from +91

matches = patt.finditer(mystr)
for match in matches:
    print(match)


# Search() :
# Search the string to see if it starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)   #star with The and then any charater end with Spain and ahead 0 or more character
# print(x)

# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned
# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)

#Findall():
# The findall() function returns a list containing all matches.
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# Return an empty list if no match was found:
# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)

# Split():
# The split() function returns a list where the string has been split at each match:
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# You can control the number of occurrences by specifying the maxsplit parameter:
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)

# Sub():
# The sub() function replaces the matches with the text of your choice:
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

# You can control the number of replacements by specifying the count parameter:
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)


# Note: If there is no match, the value None will be returned, instead of the Match Object
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x) #this will print an object

# The Match object has properties and methods used to retrieve information about the search, and the result:
#
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())