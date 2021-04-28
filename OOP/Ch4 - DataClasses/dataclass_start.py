from dataclasses import dataclass


# TODO - create a dataclass... this is started in py version 3.7, these are usual class only.. so you can add any
#  function to dataclass also
@dataclass()
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title} by {self.author} which costs {self.price}"

    # TODO - use __str__ method, magic method, returns string
    def __str__(self):
        return f"{self.title} by {self.author} ,costs {self.price}"


b1 = Book("War N Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("Wings of Fire", "APJ Abdul Kalam", 445, 29.95)
b3 = Book("War N Peace", "Leo Tolstoy", 1225, 39.95)

# print(b1.price)
# print(b2.title)


# # TODO - dataclass auto imports __repr__ function
# print(b1)
#
# # TODO - dataclass auto imports __eq__ function, this is so cooooolll!!!
# print(b1 == b3)

# TODO - use the new func present in dataclass

# change the values in run time
b1.title = "some other book"
b1.price = 34.99
print(b1)
