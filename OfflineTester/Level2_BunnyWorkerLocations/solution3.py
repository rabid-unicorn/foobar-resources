'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/tandav/google-foobar/blob/master/bunny_prisoner_locating.py"


#  Mod:
#  - Return string instead of int

def answer(x, y):
	return str(int(x * (x + 1) / 2 + (y -1)*x + (y - 2)*(y - 1) / 2))
