

from read import read_input
from algorithm import calc_books
from write import create_output
import result
import library
import book

input_filename = 'b_small.in'

results = calc_books()
create_output(results, input_filename)
