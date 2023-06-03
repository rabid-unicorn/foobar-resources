'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/oneshan/foobar/blob/master/queue_to_do/solution.py"


"""
Use bulk_xor to speed up xor calculate.
Let f(x) = 1 ^ 2 ^ 3 ^ ... ^ x
Then, xor all integers in the range from m to n = f(n) ^ f(m-1)
"""


def answer(start, length):

    def bulk_xor(m, n):
        # f(x) = 1 ^ 2 ^ 3 ^ ... ^ x
        # bulk_xor(m, n) = m ^ m+1 ^ m+2 ... ^ n = f(n) ^ f(m-1)
        m -= 1
        f_m = [m, 1, m + 1, 0][m % 4]
        f_n = [n, 1, n + 1, 0][n % 4]
        return f_m ^ f_n

    xor = 0
    for i in range(length):
        xor ^= bulk_xor(start, start + length - i - 1)
        start += length

    return xor
