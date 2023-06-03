'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level1_PrisonLaborDodgers/prisonLaborDodgers.py"


#  Description of algorithm:
#     The strategy to identify the unique ID is to sort the two lists of
#     ID's and then do an element-wise comparison of elements in the
#     two lists until the first mis-match is found.  That mis-match is
#     the unique ID.  The unique ID can be in either input lists.  The
#     list with the unique ID is the longer list.

#     This solution has two phases.  The second phase identifies the
#     the unique element.  The first phase speeds up and simplifies the
#     second phase by normalizing the input.  In this case, input
#     normalization consists of sorting the input lists and putting the
#     shorter input into a specific list 's_list' and the longer (which
#     has the unique ID) into 'l_list'.  The unique ID will be in
#     'l_list'.

#  Time and space complexity of the solution:
#     The normalization process consists of sorting and making a copy
#     of the input lists.  If N is the total number of elements in the
#     two lists, sorting has O(N log N) time complexity and the copy has
#     O(N) space complexity.  The second phase consists of a scan through
#     the two lists which has O(N) time complexity and requires O(1)
#     additional space.

#     Combining the complexities of the two phases gives O(N log N) time
#     and O(N) space complexity.

#  Assumptions/restrictions:
#      None.

#   This solution is completely of my own conception and execution.

def solution(x, y):

    #  Get sorted copies of the inputs with the longer version in 'l_list' and shorter in 's_list'
    if len(x) > len(y):
        l_list = sorted(x)
        s_list = sorted(y)
    else:
        s_list = sorted(x)
        l_list = sorted(y)

    #  Find the first index idx where s_list[idx] != l_list[idx].  The unique ID will be l_list[idx]
    for idx in range(len(s_list)):
        if (s_list[idx] != l_list[idx]):
            return l_list[idx]

    #  The above loop compares all but the last element of the long list but did not find
    #  a unique element.  If it did not identify a unique element, then the unique element
    #  is the last element in l_list.
    return l_list[-1]
