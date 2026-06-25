class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} issued")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)

# Example usage
lib = Library()
lib.add_book("Python Basics")
lib.issue_book("Python Basics")
lib.return_book("Python Basics")
