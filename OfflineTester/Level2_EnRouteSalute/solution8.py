'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/Shisir/2fc55ec2c874d8b8f5ed727ddb68acb6"


def answer(s):
    ans = cnt = 0
    for i in s:
        if i == '<':
            ans += cnt;
        elif i == '>':
            cnt += 1
    return ans << 1
