class Book:
    favs = []

    @staticmethod
    def read_books_from_file():
        books = []
        # return [Book("Goodnight Moon", 30), Book("Are You My Mother", 72)]
        file = open("input.txt", "r")
        data = file.read().split("\n")
        file.close()
        for book in data:
            book_data = book.split("\t")
            if book.strip():
                books.append(Book(book_data[0], int(book_data[1])))

        return books

    @staticmethod
    def write_books_to_file(books):
        file = open("input.txt", "w")
        for book in books:
            file.write(f"{book._title}\t{book._pages}\n")
        file.close()

    def __init__(self, title, pages):
        self._title = title
        self._pages = pages

    def __str__(self):
        return f"{self._title}, {self._pages} pages long"

    def __eq__(self, other):
        return self._title == other._title and self._pages == other._pages

    # def __hash__(self):
    #     return hash(self._title)
    __hash__ = None

    def __repr__(self):
        return str(self)

    def is_short(self):
        return self._pages < 60
