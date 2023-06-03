'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/fox0088/hey-i-already-did-that/blob/master/HeyIAlreadyDidThat.py"


def solution(n,b):
    k=len(n)
    zlist=[]
    while True:
        x = ''.join(sorted(n,reverse=True))
        y = ''.join(sorted(n))
        z10 = int(x,b) - int(y,b)
        if b!=10: n = toBaseN(z10,b)
        else: n=str(z10)
        if len(zlist)<k: n = n.zfill(k)
        if n in zlist: return len(zlist)-zlist.index(n)
        zlist.append(n)
        
def toBaseN(num,b):
    baseNnum=[]
    while num:
        baseNnum.insert(0,str(num%b))
        num=num//b
    return ''.join(baseNnum)
