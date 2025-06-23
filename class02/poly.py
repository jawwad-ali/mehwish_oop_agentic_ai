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


# Inheritance
# Parent/Super class
class Person():
    def __init__(self, name, email, nic ):
        self.name = name
        self.nic = nic
        self.email = email

    def walk(self):
        return 'I can Walking...........'
    

# Child/Derived
class Librarian(Person):
    def __init__(self, name, email, nic, emp_id, salary): # Librarian class constructor
        super().__init__(name, email, nic) # Parent class Constructor

        self.emp_id = emp_id
        self.salary = salary

    # Method Overriding
    def walk(self):
        return 'I am Running......'

lib1 = Librarian('Smith', 'smith@gmail.com', 1351265987398, 990, "USD 1000" )
print(lib1.email)
print(lib1.walk())

class Member(Person):
    def __init__(self, mem_id, name, email, nic ):
        self.emp_id = mem_id
        self.name = name
        self.email = email
        self.nic = nic

mem1 = Member(9809, 'James', 'james@yahoo.com', 88484802392423489)

