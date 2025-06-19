class Book():
    # constructor
    def __init__(self, title: str, author: str):
        # self.<variable_name> represent at class level
        # title represents the book title at object

        self.book_title = title
        self.book_author = author

    def borrow(self, book_name: str):
        print(f'Borrowing book {book_name}')

    def return_book(self):
        print('Returning book')

book1 = Book('1984', 'George Orwell') # Creating an instance of Book
book2 = Book('To Kill a Mockingbird', 'Harper Lee') # Another instance

print(book1.book_title)

book1.borrow(book1.book_title)

book1.borrow(book2.book_title)
