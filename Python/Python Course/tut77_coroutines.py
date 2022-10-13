"""
Coroutines are mostly used in cases of time-consuming programs,
such as tasks related to machine learning or deep learning algorithms or in cases where the program has to read a file containing a large number of data.
In such situations, we do not want the program to read the file or data,
again and again, so we use coroutines to make the program more efficient and faster.
Coroutines run endlessly in a program because they use a while loop with a true or 1 condition so it may run until infinite time.
Even after yielding the value to the caller,
it still awaits further instruction or calls. We have to stop the execution of coroutine by calling coroutine.close() function.
It is very crucial to close a coroutine because its continuous running can take up memory space

Coroutine Execution:-
Execution is the same as of a generator. When you call a coroutine, nothing happens.
They only run in response to the next() and send() methods.
Coroutine requires the use of the next statement first so it may start its execution.
Without a next() it will not start executing.
We can search a coroutine by sending it the keywords as input using object name along with send().
The keywords to be searched are send inside the parenthesis.

When we run the next() function the first time, the coroutine executes and waits for new input.
After the input is sent to it using the send() function, it executes it and again waits for next input,
and the process goes on like this because we have set the while loop as true, so it will never exit its execution.
In order to make the execution stop, we have to close the coroutine using coroutine.close() function.

send() — used to send data to coroutine
 close() — to close the coroutine

"""


def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on Earth and code with me and good feel"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


# when coroutine star it stop at while loop  and send() come it star again it come again it again start from while
search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("keyur")

search.send("keyur as per")
# input("press any key")
# search.send("keyur and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")

search.close()