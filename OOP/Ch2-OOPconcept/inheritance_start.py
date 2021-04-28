# TODO : understanding inheritance

class Book:
    def __init__(self, title, author, page, price):
        self.title = title
        self.author = author
        self.page = page
        self.price = price


class Magazine:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period


class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period
