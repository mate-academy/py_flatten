"""module docstring"""


def flatten(*array):
    """func docstring"""
    a_string = "".join(str(array))
    improved_arr = []
    for seq, value in enumerate(a_string):
        if value.isnumeric():
            improved_arr += value
    for seq, value in enumerate(improved_arr):
        improved_arr[seq] = int(value)

    return improved_arr
