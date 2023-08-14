class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book1 = Book("On Liberty", "Mill")
book1.author = "John Stuart Mill"
print(book1.title)
print(book1.author)
book2 = Book("The Last Casualty", "Ben Elton")
book2.title = "The First Casualty"
print(book2.title)
print(book2.author)