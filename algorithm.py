from typing import Dict
import bisect
from result import Result
from library import Library


def calc_books():
    result1 = Result(Library(1, 0, 0, 0), [5, 2, 3], 10)
    result2 = Result(Library(0, 0, 0, 0), [1, 2, 3, 4, 5], 10)
    return [result1, result2]
