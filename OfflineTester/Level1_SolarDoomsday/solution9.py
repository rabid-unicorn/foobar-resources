'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gitlab.com/DevAlone/google_foobar_solutions/-/blob/master/level%201/Solar%20Doomsday/main.py"


import math
import sys


def answer(n):
    result = []
    while n > 0:
        part = int(math.sqrt(n))
        part *= part
        
        if part:
            result.append(part)
        else:
            result.append([1] * part)
            break
        
        n -= part
        
    return result
