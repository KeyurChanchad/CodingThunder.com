
import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        # if i want extension of any file  main.txt
        # 1. os.path.splitext(file)[1]  [main, txt]  txt == format
        if os.path.splitext(file)[1] == format:      #file.endswith(format)
            print(os.path.splitext(file)[1])
            os.rename(file, f"{i}{format}")
            i +=1

# r"" string is use for slashing escap sequence character string path
soldier(r"C:/Users/Lenovo/Desktop/That",
        r"C:/Users/Lenovo/Desktop/That/main.txt", ".jpg" )