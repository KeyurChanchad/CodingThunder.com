"""
What Is a Command Line Utility?
A command-line utility is a way of giving operating system instructions using lines of texts.
Command-line programs operate via command line or PowerShell. It will interact with a command-line script.

argsparse helps us to get command-line arguments in our program,
and the sys module helps us to import the code we wrote using argparse onto the console.
For more details and descriptions about these modules, you can read the python documentation for these modules.

"""
import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact keyur bhai")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact keyur bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact keyur bhai for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    # sys.standardoutput.write it take string
