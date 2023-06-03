'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/oneshan/foobar/blob/master/bomb_baby/solution.py"


"""
Suppose M > F, to hit (M, F), last state must be (M-F, F).

We can use Euclidean algorithm to calcualte the generations
from (M, F) down to (1, 1)

A simple case: (1, 1)-(2, 1)-(3, 1)-(3, 4)-(7, 4)
Impossible Case: gcd(M, F) != 1
"""


def answer(M, F):
    x, y = int(M), int(F)
    count = 0
    while y >= 1:
        if x < y:
            x, y = y, x
        x, y, q = y, x % y, x // y
        count += q
    return str(count - 1) if x == 1 else "impossible"
