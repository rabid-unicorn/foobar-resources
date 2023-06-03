'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rudisimo/google-foobar/blob/master/solutions/ion_flux_relabeling/solution.py"


#  Mod:
#  - Change long types to int.


import math

def calculate_tree_size(height):
    return int(math.pow(2, height) - 1)

def shift_right_zero_fill(value, bits):
    return (value & 0xffffffff) >> bits

def find_parent(height, node):
    size = calculate_tree_size(height)
    if node == size:
        return -1

    previous = 0
    while True:
        size = shift_right_zero_fill(size, 1)
        left = previous + size
        right = left + size
        current = right + 1

        if left == node or right == node:
            return current

        if node > left:
            previous = left

    return 0

def answer(h, q):
    return [find_parent(h, n) for n in q]
