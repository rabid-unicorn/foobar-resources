'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/povstenko/bomb-baby/blob/main/solution.py"


def solution(x, y):
    M, F = int(x), int(y)
    generations = 0

    while M != F:
        if M > F:
            subs = (M-F)//F + ((M-F) % F > 0)
            generations += subs
            M -= subs * F
        else:
            subs = (F-M)//M + ((F-M) % M > 0)
            generations += subs
            F -= subs * M

    return str(generations) if (M, F) == (1, 1) else 'impossible'
