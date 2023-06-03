'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/franklinvp/foobar/blob/master/foobar2020/solutionProblem16.py"


#  Mod:
#  - Return list rather than tuple.


def solution(l, t):
    """
    We compute the sums of the prefixes of the list.
    Each time we check if the current sum minus t is a sum
    that has been seen before. If it has, the difference of those sums
    is the sum of the first contiguous sublist which sum is t.
    This solution uses O(|l|) extra memory and has amortized execution
    time in O(|l|).
    """
    if l[0] == t:
        return [1,1]
    sums = 0
    seen = {0:-1}
    for i, x in enumerate(l):
        sums += x
        seen[sums] = i
        diff = sums-t
        if diff in seen:
            return [seen[diff]+1,i]
    return [-1,-1]

