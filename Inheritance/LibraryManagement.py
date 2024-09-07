class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def displayInfo(self):
        print(f"Title {self.title}, Author {self.author}, ISBN {self.isbn}")
    
class Library:
    
    def __init__(self):
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        print(f"Book {book.title} added to the library.")
        
    def removeBook(self, isbn):
        bookToRemove = None
        for book in self.books:
            if book.isbn == isbn:
                bookToRemove = book
        if bookToRemove:
            self.books.remove(bookToRemove)
            print(f"Book {bookToRemove.title} removed from the library.")
    
    def displayBooks(self):
        if not self.books:
            print("The library is empty")
        else:
            for book in self.books:
                book.displayInfo()

class SpecialLibrary(Library):
    
    def addBook(self, book):
        super().addBook(book)
        print(f"Special handling for book {book.title}")

book1 = Book("Azure OpenAI", "Bharath", "123")
book2 = Book("AWS Lambda", "Bharath", "456")

library = Library()
library.addBook(book1)
library.addBook(book2)

library.displayBooks()

library.removeBook("123")
library.displayBooks()

specialLibrary = SpecialLibrary()
specialLibrary.addBook(book1)


