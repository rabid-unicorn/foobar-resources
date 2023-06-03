'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/lcsm29/goog-foobar/blob/main/level1/braille_translation/solution.py"


def solution(s):  # the one that I submitted on Invitation #A1
    return ''.join('000001' + braille[c.lower()] if c.isupper() else braille[c] for c in s)


braille = {
    'a': '100000', 'b': '110000', 'c': '100100', 'd': '100110',
    'e': '100010', 'f': '110100', 'g': '110110', 'h': '110010',
    'i': '010100', 'j': '010110', 'k': '101000', 'l': '111000',
    'm': '101100', 'n': '101110', 'o': '101010', 'p': '111100',
    'q': '111110', 'r': '111010', 's': '011100', 't': '011110',
    'u': '101001', 'v': '111001', 'w': '010111', 'x': '101101',
    'y': '101111', 'z': '101011', ' ': '000000'
}