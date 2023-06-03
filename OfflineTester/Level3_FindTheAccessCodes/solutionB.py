'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gitlab.com/DevAlone/google_foobar_solutions/-/blob/master/level%203/Find%20the%20Access%20Codes/main.py"


import math


def answer(l):
    result = 0
    number_of_doubles = [0 for _ in l]
    for i in range(1, len(l) - 1):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                number_of_doubles[i] += 1

    for i in range(2, len(l)):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                result += number_of_doubles[j]

    return result
