from typing import List


TYPES = ("hardcover", "paperback")


def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)


# nothing ot tell you that you might be making a mistake
# use colon and ->


class Book:
    def __init__(self, name: str, page_count: int, weight: int):
        self.name = name
        self.page_count = page_count
        self.eight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weight {self.weight} pounds"

    # have to use string for object name because you are referring to the object this method is currently in and it hasn't been createf yet
    # use quotes to signal that this method returns a book object, which returns a Book object, which is the same type that we are currenlty in

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

# can also hint for class definitions
# will get told if you pass in the wrong thing


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books"
