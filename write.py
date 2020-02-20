from datetime import datetime


def create_output(input_filename: str, score: int, pizzas):
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    filename = 'outputs/' + input_filename[:-3] + '/{} - {}.in'.format(score, current_time)
    f = open(filename, "w+")
    f.write('{}\n'.format(len(pizzas)))

    for pizza in pizzas:
        f.write('{} '.format(pizza))
