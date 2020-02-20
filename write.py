from datetime import datetime


def create_output(results, input_filename):
    score = 0

    for x in results:
        score += x.score

    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    filename = 'outputs/' + input_filename[:-3] + '/{} - {}.in'.format(score, current_time)
    f = open(filename, "w+")
    f.write('{}\n'.format(len(results)))

    for i, result in enumerate(results):
        f.write(str(result.library.id) + ' ' + str(len(result.books)) + '\n')

        book_print = ''
        for book in result.books:
            book_print += str(book.id) + ' '

        print(book_print)
        f.write(book_print[:-1])
        f.write('\n')
