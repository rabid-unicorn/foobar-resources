'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/dishbreak/48bca2c9c60420a53920c39e08d16c56"


# algorithm modified from here: https://codereview.stackexchange.com/a/150464

def get_parent_index(h, idx):
    ## calculate the maximum index first
    ## if the input is too large, return a negative 1
    max_idx = 2 ** h - 1
    if max_idx < idx:
        return -1

    # otherwise, carry on
    else:
        node_offset = 0
        continue_flag = True
        subtree_size = max_idx
        result = -1  # default result

        while continue_flag:
            if subtree_size == 0:
                continue_flag = False

            # right shift is equivalent to dividing by 2 and discarding the remainder.
            subtree_size = subtree_size >> 1

            # predict the left node
            left_node = node_offset + subtree_size

            # predict the right node
            right_node = left_node + subtree_size

            # calculate my node value
            my_node = right_node + 1

            # if either child is a match, return my node value
            if (left_node == idx) or (right_node == idx):
                result = my_node
                continue_flag = False

            # Make the current left child the offset if the index is greater than the left.
            # This effectively searches down the right subtree.
            if (idx > left_node):
                node_offset = left_node

        return result


def answer(h, q):
    return [get_parent_index(h, x) for x in q]
