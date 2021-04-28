from dataclasses import dataclass, field
import random


# TODO - create a dataclass... this is started in py version 3.7, these are usual class only.. so you can add any
#  function to dataclass also


def price_info():
    return float(random.randint(20, 40))


@dataclass()
class Book:
    title: str = "No Title"
    author: str = "No author"
    pages: int = 0
    price: float = 0.0


#b1 = ("some book", "shekar", 1223)
b1 = Book()  # using default values
print(b1)
