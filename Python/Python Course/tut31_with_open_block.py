with open("keyur.txt") as f:
    a = f.readlines()
    print(a)

# f = open("keyur.txt", "rt")
# Question of the day  why we need to close file pointer- Yes or No and why?
# because of all file resource need to free
# f.close()

# With open(“file1txt”) as f, open(“file2.txt”) as g
