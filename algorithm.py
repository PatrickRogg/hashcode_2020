from book import Book
from library import Library
from result import Result


def calc_books(libraries, remaining_days: int):
    results = []
    prev_signup_time = 0
    while remaining_days > 0 and len(libraries) > 0:
        library = get_best_library(libraries, prev_signup_time)
        results.append(Result(library, library.books_set[:remaining_days], library.remaining_score))
        remaining_days -= library.signup_time
        prev_signup_time = library.signup_time

    return results


def get_best_library(libraries, prev_signup_time):
    max_library: Library = None

    for library in libraries:
        calc_remaining_library_score(library, prev_signup_time)

        if max_library is None or max_library.remaining_score < library.remaining_score:
            max_library = library
        elif library.remaining_score == 0:
            libraries.remove(library)

    if max_library.remaining_score != 0:
        libraries.remove(max_library)

    return max_library


def calc_remaining_library_score(library: Library, prev_signup_time: int):
    to_remove_books = prev_signup_time * library.number_books_per_day
    start_index = len(library.books_set) - 1 - to_remove_books

    if start_index < 0:
        library.remaining_score = 0
        return

    for i in range(start_index, len(library.books_set)):
        book: Book = library.books_set[i]
        library.remaining_score -= book.score
