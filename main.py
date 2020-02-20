from typing import Dict

from algorithm import calc_pizzas
from read import read_input
from write import create_output

input_filename = 'b_small.in'
pizza_input = read_input(input_filename)
max_slices = pizza_input[0]
pizzas = pizza_input[1]

slices_to_pizza_index: Dict = {}

for index, pizza in enumerate(pizzas, start=0):
    if pizza in slices_to_pizza_index:
        slices_to_pizza_index[pizza].append(index)
    else:
        slices_to_pizza_index[pizza] = [index]

result_pizzas_and_score = calc_pizzas(slices_to_pizza_index, max_slices)
create_output(input_filename, result_pizzas_and_score[1], result_pizzas_and_score[0])
