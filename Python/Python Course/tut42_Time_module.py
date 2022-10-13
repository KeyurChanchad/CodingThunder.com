import time
seconds = time.time()
print("Seconds since epoch  miliseconds=", seconds)
# time.asctime()
# time.sleep(5)

# time localtime():
print(time.localtime(seconds) )
# print ("time.localtime() returns: %s", %time.localtime())

initial = time.time()
#
# k = 0
# while (k < 45):
#     print("I am keyur bhai")
#     time.sleep(2)
#     k += 1
# print("While loop ran in", time.time() - initial, "Seconds")
#
# initial2 = time.time()
# for i in range(45):
#     print("This is keyur bhai")
# print("For loop ran in", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)




