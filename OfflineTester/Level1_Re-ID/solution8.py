'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/pketanp/google-foo-bar-1st-challenge/blob/master/solution%2Cpy"


def isPrime(n):
    p=True
    for i in range(2, n):
        if (n % i) == 0:
            p=False
            break
    return p
def nextPrime(n):
    prime = n
    while(True):
        prime = prime + 1
        if(isPrime(prime) == True):
            break
    return prime
def solution(i):
    a=[2]
    if i==0 or i==1 :
        g=5
    else:
        g=i+3
    for l in range(g):
        n = a[-1]
        n=nextPrime(n)
        a.append(n)
    b = "".join(map(str, a))
    return b[i:i+5]
