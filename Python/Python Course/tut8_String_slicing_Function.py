mystr = "keyur is a Good boy and Nice person"
# Indexing
# print(mystr)     #print full string
# print(mystr[0])   #print single character
# print(mystr[45])    # its  throw an error because of there is noting in index number 45
# print(mystr[0:45])      # it start with 0 and goes upto 45 it is not than print upto length
# print(len(mystr))     # return length

# Slicing
# print(mystr[0:16])
# print(mystr[0:36])   #  print index number 0 to index number 36 it's length
# 0 index is include and 36 is exclude
# print(mystr[0:])      # By default it take length
# print(mystr[:36])     # by default it start with 0 index
# print(mystr[:])          # This means mystr[0:length]

# print(mystr[::1])       # third number is jump 1 character
# print(mystr[::])        # By default it 1
# print(mystr[0:36:2])      # it skip 1 character and jump 2
# print(mystr[::2])
print(mystr[-5:0])      #slicing is not perfoming in reverse order
print(mystr[-11:])
print(mystr[-6:-2])
print(mystr[24:36])
print(mystr[::-1])      # when third number is nagative it start in reverse
print(mystr[::-2])

#Function
str= "12324"
print(mystr.isalnum())    # if it is alpha and numeric it return true
print(str.isalnum())        # str is numeric
print(mystr.isalpha())
print(mystr.endswith("person"))
print(mystr.strip())
print(mystr.startswith("ram"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is", "are"))
