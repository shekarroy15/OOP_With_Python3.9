# TODO : understanding inheritance
# TODO : Too much boiler plate code, can be cleaned up by inheriting from another set of class


class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        Publication.__init__(self, title, price)
        self.publisher = publisher
        self.period = period


class Book(Publication):  # inheritance in play
    def __init__(self, title, author, page, price):
        Publication.__init__(self, title, price)  # inheritance in play
        self.author = author
        self.page = page


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        Periodical.__init__(self, title, publisher, price, period)  # inheritance in play


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        Periodical.__init__(self, title, publisher, price, period)  # inheritance in play


b1 = Book("Me", "Shekar", 34, 2003)
b2 = Book("Me", "Shekar", 34, 2003)
n1 = Book("Me", "Shekar", 34, 1999)

print (n1.price)
print (b1.price)
