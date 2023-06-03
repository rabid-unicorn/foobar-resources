'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/imvaibhavm/Disorderly_Escape/blob/master/Disorderly_Escape.py"


#  Mod:
#  - Convert answer to string upon return to caller.


from collections import Counter

def answer(w, h, s):    
    grid=0
    for pw in partitions(w):
        for ph in partitions(h):            
            m=count(pw, w)*count(ph, h)
            grid+=m*(s**sum([sum([gcd(i, j) for i in pw]) for j in ph]))
              
    return str(grid//(factorial(w)*factorial(h)))
    
def count(c, n):
    cnt=factorial(n)
    for a, b in Counter(c).items():
        cnt//=(a**b)*factorial(b)
    return cnt        

def partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in partitions(n-i, i):
            yield [i] + p

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
