# f = open("keyur.txt", "w")  # Open function return file handler
# a = f.write("Keyur bhai bahut achhe hain\n")    # write function return number of character
# print(a)
# f.close()
#
# f = open("keyur.txt", "a")
# a = f.write("Lord Indra is king of gods and goddess\n")
# print(a)
# f.close()


# Handle read and write both
f = open("keyur.txt", "r+")
print(f.read())
f.write("thank you")

