from dataclasses import dataclass


# TODO - create a dataclass... this is started in py version 3.7, these are usual class only.. so you can add any
#  function to dataclass also
@dataclass()
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO - post init will get executed after the default init func of the dataclass is done..
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, has {self.pages} pages"


b1 = Book("War N Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("Wings of Fire", "APJ Abdul Kalam", 445, 29.95)

# TODO - description is accessed from the post init func
print(b1.description)
print(b2.description)

