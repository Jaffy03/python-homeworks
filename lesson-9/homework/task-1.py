class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class MemberNotFoundException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum number of books (3).")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True
        print(f"{self.name} has borrowed '{book.title}'.")
    
    def return_book(self, book):
        if book not in self.borrowed_books:
            raise BookNotFoundException(f"{self.name} did not borrow '{book.title}'.")
        self.borrowed_books.remove(book)
        book.is_borrowed = False
        print(f"{self.name} has returned '{book.title}'.")
    
    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")
    
    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")
    
    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise MemberNotFoundException(f"Member '{name}' not found.")
    
    def borrow_book(self, member_name, book_title):
        try:
            member = self.find_member(member_name)
            book = self.find_book(book_title)
            member.borrow_book(book)
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException, MemberNotFoundException) as e:
            print(f"Error: {e}")
        
    def return_book(self, member_name, book_title):
        try:
            member = self.find_member(member_name)
            book = self.find_book(book_title)
            member.return_book(book)
        except (BookNotFoundException, MemberNotFoundException) as e:
            print(f"Error: {e}")
    
    def __str__(self):
        return f"Library: {len(self.books)} books, {len(self.members)} members"


if __name__ == "__main__":
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book4 = Book("Moby Dick", "Herman Melville")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "Moby Dick")  
    library.borrow_book("Bob", "1984")  

    library.return_book("Alice", "1984")
    library.return_book("Alice", "1984")  

    print(library)
    print(member1)
    print(member2)