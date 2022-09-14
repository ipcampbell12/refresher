class Book:
    TYPES = ('Hardcover', 'Paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    # print out string representation of book object -
    def __repr__(self):
        return f"Book {self.name}, {self.book_type}, weighing {self.weight}"

    # can validate what the book type is
    # can say cls instead of class name
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


#book1 = Book('Harry Potter', 'Hardcover', 1500)

# don't have to pass type
book1 = Book.hardcover('Harry Potter', 1500)
book2 = Book.paperback('Hunger Games', 1200)

print(book1)
print(book2)
