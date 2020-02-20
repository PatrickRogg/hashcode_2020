from typing import Dict
import bisect


def calc_pizzas(slices_to_pizza_index: Dict, max_slices: int):
    curr_slices = 0
    slices = []

    while True:
        keys = list(slices_to_pizza_index.keys())
        next_idx = bisect.bisect_left(keys, max_slices - curr_slices)
        key = keys[next_idx - 1]

        if curr_slices + key > max_slices:
            break

        curr_slices += key
        remaining_size = len(slices_to_pizza_index[key]) - 1
        slices.append(slices_to_pizza_index[key][remaining_size])

        if remaining_size > 0:
            slices_to_pizza_index[key] = slices_to_pizza_index[key][:-1]
        else:
            slices_to_pizza_index.pop(key, None)

    return slices, curr_slices
