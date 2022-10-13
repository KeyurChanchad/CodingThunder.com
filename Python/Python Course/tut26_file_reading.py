# f = open("keyur.txt", "rt")   # this is default mode  read and text
# f = open("myfile.txt", "r")
# print(f.read(6))     #Here, you will get the first 6 characters of the file.
# print(f.read())

f=open("myfile.txt", "r")
# f.readlines() #Returns a list object

# print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())
content = f.read()

# when file handler deal with other it's not working in for loop
for line in f:
    print(line, end="")

# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()
f.close()