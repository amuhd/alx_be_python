class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"{title} has been checked out.")
                    return True
                else:
                    print(f"{title} is already checked out.")
                    return False
        print(f"{title} not found in the library.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned.")
                    return True
                else:
                    print(f"{title} was not checked out.")
                    return False
        print(f"{title} not found in the library.")
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books after setup:")
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books available.")


# Example:
if __name__ == "__main__":
    library = Library()
    
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")
    
    library.add_book(book1)
    library.add_book(book2)
    
    library.list_available_books()
    
    library.check_out_book("1984")
    library.list_available_books()
    
    library.return_book("1984")
    library.list_available_books()
    
    library.check_out_book("The Catcher in the Rye")
    library.return_book("The Catcher in the Rye")
