from book import Book
from library import Library
from result import Result


def calc_books():
    result1 = Result(Library(1, 0, 0, 0), [Book(2, 2), Book(5, 5)], 10)
    result2 = Result(Library(0, 0, 0, 0), [Book(1, 1), Book(3, 2), Book(4, 3), Book(6, 4), Book(7, 5)], 10)
    return [result1, result2]
