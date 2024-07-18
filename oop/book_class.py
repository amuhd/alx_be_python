class Book:
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with the given title, author, and publication year.
        
        :param title: The title of the book.
        :param author: The author of the book.
        :param year: The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when a Book instance is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a string representation of the Book instance in the format:
        "(title) by (author), published in (year)"
        
        :return: A string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can be used to recreate
        the Book instance.
        
        :return: A string that represents the constructor of the book.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)
    print(str(book))  # Output: 1984 by George Orwell, published in 1949
    print(repr(book))  # Output: Book('1984', 'George Orwell', 1949)

    # Deleting the book instance to see the __del__ method in action
    del book
