class Book:
    # class properties, data stored inside the class itself
    TYPES = ('Hardcover', 'Paperback')

    # instance method
    # create an object with values that are stored inside properties of object itself
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    # print out string representation of book object -
    # representation of book object with all the data include inside that would allow us to recreate the book object
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"

    # can validate what the book type is - make sure it's only ever hardcover or paperback (not comic book for example)
    # can say cls instead of class name
    # creates new book object of type hardcover
    # access the class itself inside the method to create
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


#book1 = Book('Harry Potter', 'Hardcover', 1500)

# don't have to pass type, type is added inside the method
book1 = Book.hardcover('Harry Potter', 1500)
book2 = Book.paperback('Hunger Games', 1200)

print(book1)
print(book2)
