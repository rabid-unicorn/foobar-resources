'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://randomds.com/2022/01/21/google-foobar-challenge-level-2-numbers-station-coded-messages"


# Mod
# - Return lists

def solution(l, t):
    # Setup each list element as
    # potential starting point
    for i in l:
        # Initialize the sum at 0 every time
        tot = 0
        # Setup each following element to
        # be added
        for j in range(i, len(l)):
            # Increase the total
            tot += l[j]
            # If total is equal to target
            if tot == t:
                # Return start and end index
                return [i, j]
            # If total is above target
            if tot > t:
                # Break the loop and move to
                # next item
                break
    # If we did not find a sequence that
    # adds up to the target, return -1,-1
    return [-1, -1]
