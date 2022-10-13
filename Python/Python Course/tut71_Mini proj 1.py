# Create a library class
#     display book
#     lend book  (who owns the book if not present)
#     add book
#     return book

# keyur_library = Library(listofbook, library name)

#dictionary  (books-nameofperson)
# Create a main function and run an infinite while loop asking  users for their input

class Library:
    allocater_name = " "
    book_dict = {}
    books = ["Bhagawat geeta"]

    def __init__(self, lob, lib_name):

        self.books = lob
        self. lib_name = lib_name

    @classmethod
    def add_book(cls, book_name):
        cls.books.append(book_name)

    @classmethod
    def display_book(cls):
        # print(cls.books)
        print("~~~~~~~~~~~")
        for book in cls.books:
            print(book)
        print("~~~~~~~~~~~")

    @classmethod
    def allocate_book(cls, book, name):
        cls.allocater_name = name
        cls.books.remove(book)
        cls.book_dict[book] = name
        print(f"This {book} book is allocate to you..")

    @classmethod
    def return_book(cls, book):
        del cls.book_dict[book]
        cls.add_book(book)
        print("Returned ...")

    @classmethod
    def lend_book(cls, book):
        if cls.books.__contains__(book):
            print("The book is available...")
        else:
            print(f"The book is allocate to {cls.book_dict[book]}")





listofbook = ["cpp", "java"]
keyur_library = Library(listofbook, "My library")

if __name__ == '__main__':
     while(1):
        print("1 for Display books")
        print("2 for Lend books")
        print("3 for Add books")
        print("4 for allocate book")
        print("5 for Return books")
        print("6 for Exit")

        ch = int(input("Enter your choice: "))

        if(ch == 1 ):
            keyur_library.display_book()

        elif ch == 2:
            book = str(input("Enter book name that you want it: "))
            keyur_library.lend_book(book)

        elif ch == 3:
            book = str(input("Enter book name: "))
            keyur_library.add_book(book)

        elif ch == 4 :
            name =  str(input("Enter name: "))
            book = str(input(f"Enter book name that you want to give {name}. "))
            keyur_library.allocate_book(book,name)

        elif ch == 5:
            book = str(input("Enter book name: "))
            keyur_library.return_book(book)

        elif ch == 6:
            break
