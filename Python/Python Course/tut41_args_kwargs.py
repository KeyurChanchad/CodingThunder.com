# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)
#
# function_name_print("Keyur", "Kishan", "Dwarkesh", "Nayan", "Jalal")

def funargs(normal, *argskeyur, **kwargsbala):    # it must be in order args, kwargs or normal, args, kwargs or normal, kwargs
    print(normal)
    for item in argskeyur:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")



harhar = ["Keyur", "Krishan", "Skillf", "Mahammad", 25, 36.2556,
       "Jalal", "The programmer"]
normal = "I am a normal Argument and the students are:"
mahadev = {"Jarvis": "Monitor", "Prashant": "Fitness Instructor",
      "The Programmer": "Coordinator", "Keyur": "Cook"}
funargs(normal, *harhar, **mahadev)

