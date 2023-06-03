'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://livecodestream.dev/challenge/the-grandest-staircase-of-them-all"


def solution(n):
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    m[0][0] = 1  # base case
    for stair in range(1, n + 1):
        for left in range(0, n + 1):
            m[stair][left] = m[stair - 1][left]
            if left >= stair:
                m[stair][left] += m[stair - 1][left - stair]

    return m[n][n] -1
