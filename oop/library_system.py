class Book:
    def __init__(self, title, author):
        """
        Initializes a Book instance with the given title and author.
        
        :param title: The title of the book.
        :param author: The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book instance.
        
        :return: A string representing the book's title and author.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance with the given title, author, and file size.
        
        :param title: The title of the ebook.
        :param author: The author of the ebook.
        :param file_size: The size of the ebook file in MB.
        """
        super().__init__(title, author)
        self.file_size = "File Size"

    def __str__(self):
        """
        Returns a string representation of the EBook instance.
        
        :return: A string representing the ebook's title, author, and file size.
        """
        return f"EBook: {super().__str__()}, {self.file_size:}: 500KB" 


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance with the given title, author, and page count.
        
        :param title: The title of the print book.
        :param author: The author of the print book.
        :param page_count: The number of pages in the print book.
        """
        super().__init__(title, author)
        self.page_count = "Page Count"

    def __str__(self):
        """
        Returns a string representation of the PrintBook instance.
        
        :return: A string representing the print book's title, author, and page count.
        """
        return f"PrintBook: {super().__str__()}, {self.page_count:}: 234 "


class Library:
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook) to the library.
        
        :param book: The book instance to add to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        for book in self.books:
            print(book)

