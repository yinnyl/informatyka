class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def print_book(self):
        print(self.title, self.author, self.year, self.is_available)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.print_book()

    def borrow_book(self, title):
        borrowed = False
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                borrowed = True
        return borrowed

    def return_book(self, title):
        returned = False
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                returned = True
        return returned

book01 = Book("Igrzyska śmierci", "Suzanne Collins", 2008)
book02 = Book("Biblioteka o północy", "Matt Haig", 2021)

library = Library()
library.display_books()

library.add_book(book01)
library.add_book(book02)
library.display_books()
library.borrow_book("Biblioteka o północy")
library.display_books()