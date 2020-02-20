from read import read_file
from algorithm import calc_books
from write import create_output

#input_filename = 'a_example.txt'
#input_filename = 'b_read_on.txt'
#input_filename = 'c_incunabula.txt'
#input_filename = 'd_tough_choices.txt'
#input_filename = 'e_so_many_books.txt'
input_filename = 'f_libraries_of_the_world.txt'

input = read_file(input_filename)
results = calc_books(input[0], input[1])
create_output(results, input_filename)