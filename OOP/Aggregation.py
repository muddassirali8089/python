



class Library:
    def __init__(self , name):
        self.name = name
        self.books = []

    def addBook(self , book):
        self.books.append(book)

    def displayBooks(self):
        return[f"{book.name} by {book.author}" for book in self.books]

class Book:
    def __init__(self , name , author):
        self.name = name
        self.author = author




book1 = Book("muddassir" , "programing fundametals")
book2 = Book("book name" , "book title")

library = Library("bacha khan")
print(library.name)

library.addBook(book1)
library.addBook(book2)
for book in library.displayBooks():
    print(book)


        