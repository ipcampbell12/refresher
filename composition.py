class BookShelf:
    # takes a bunch of book objects
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"


shelf = BookShelf(300)

print(shelf)


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Your Mom's Pretty Good Book")

# give books to bookshelf (no inheritance)
shelf = BookShelf(book, book2)

print(shelf)
