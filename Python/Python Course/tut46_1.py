# print("__name__ in tut46_1.py is set to"+__name__)

def print_details(string):
    return  f"Ye string keyur ko de de thakur {string}"

def add(num1, num2):
    return num1 + num2 + 3

print("This file is executed in ", __name__)
# OUTPUT : This file is executed in  __main__
# __name__ is __main__ when the file executed in which  __name__ == '__main__': is there


# if we write if __name__ == '__main__':  it ignore by other file who import this file
if __name__ == '__main__':      # write by main
    print(print_details("King of hindustan"))
    a  = add(55,2)
    print(a)