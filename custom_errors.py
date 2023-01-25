# needs to inherit from any (or most relevant) built in error or exception class
# copy of value error but with a different name
# don't ususally need to write too much in custom error classes
class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"
        )

    def read(self, pages: int):
        # add custom error to keep you from reading too many pages

        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages"
            )

        self.pages_read += pages
        print(
            f"You have now read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python 101", 50)
# python101.read(35)

# # can't do this, but the program can't stop you!
# python101.read(50)


# make it nicer for users

try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)