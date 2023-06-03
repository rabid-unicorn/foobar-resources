'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rudisimo/google-foobar/blob/master/solutions/prison_labor_dodgers/solution.py"


def answer(x, y):
    # find symmetric difference between the two sets
    diff = list(set(x) ^ set(y))
    # return fist item in output list
    return diff[0]
