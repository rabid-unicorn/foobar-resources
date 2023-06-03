'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.oasys.net/posts/google-foobar-programming-challenge"


from math import sqrt

def solution(area):
    # return list of the areas of the largest squares
    # that can be made out of the provided area, largest first
    if area < 1 or area > 1000000:
        raise ValueError("area should be between 1 and 1000000 inclusive")
    if sqrt(area).is_integer():
        return [area]
    biggest = int(sqrt(area)) ** 2
    return [biggest] + solution(area - biggest)
