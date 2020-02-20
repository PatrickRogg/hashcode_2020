from book import Book
from library import Library
import operator


def read_file(filename):
    file = open('datasets/{}'.format(filename), 'r')
    lines = file.readlines()

    remaining_days = [int(i) for i in lines[0].split()][2]

    books_score_input = lines[1].split()
    #print(books_score_input)
    books = []
    book_id_to_book = {}

    for i, score in enumerate(books_score_input):
        book = Book(i, int(score))
        books.append(book)
        book_id_to_book[i] = book

    #sorted_books = sorted(books, key=operator.attrgetter('score'), reverse=True)

    libraries_input = lines[2:]
    libraries = []
    for i in range(0, len(libraries_input), 2):
        try:
            libraries_input[i + 1]
        except:
            break
        library_book_ids = libraries_input[i + 1].split()
        print(library_book_ids)
        books_of_library = []
        initial_score = 0
        j = 0
        library_input = [int(i) for i in libraries_input[i].split()]

        max_days = (remaining_days - library_input[1]) * library_input[2]

        for book_id_as_string in library_book_ids:
            book_id = int(book_id_as_string)
            books_of_library.append(book_id_to_book[book_id])

            if j < max_days:
                initial_score += book.score

        library = Library(i % 2, books_of_library, library_input[1], library_input[2], initial_score)
        libraries.append(library)

    return libraries, remaining_days