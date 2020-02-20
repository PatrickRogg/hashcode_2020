def read_input(filename):
    file = open('datasets/{}'.format(filename), 'r')
    lines = file.readlines()
    max_slices = int(lines[0].split()[0])
    pizzas = [int(i) for i in lines[1].split()]

    return max_slices, pizzas
