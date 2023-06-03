'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/bphiett/google.foo.bar.ion_flux_relabelling/blob/master/solution.py"


def heightToSize(height):

    n = (2**height)-1
    return n

def findParent(root, height, node, parent=-1):

    if node != root:
        parent = root
        right_child = root-1
        left_child = root-(2**(height-1))
        height-=1
        
        if node > left_child:
            # node in right subtree
            root = right_child
            parent = findParent(root, height, node, parent)
        else:
            # node in left subtree
            root = left_child
            parent = findParent(root, height, node, parent)
            
    return parent
        
def solution(h, q):
    # for a tree of given height (h), return parent values for values of interest (q)

    n = heightToSize(h)
    p = [findParent(n, h, value) for value in q]
    return p
