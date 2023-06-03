'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html"


#  Mod:
#  - Use numpy's version of LCM instead of Fraction's version (which
#    was removed from Fraction after Python 3.4).


from fractions import Fraction
import numpy as np

def solution(m):
    if len(m) < 2:
        return [1,1]
    r_subm, q_subm = split_martix(m)
    f_subm = calc_f(q_subm)
    fr_subm = np.dot(f_subm, r_subm)
    return dec_to_frac_with_lcm(fr_subm[0])

def split_martix(m):
    absorbing = set()
    for row_i in range(len(m)):
        if sum(m[row_i]) == 0:
            absorbing.add(row_i)
    r_subm = []
    q_subm = []
    for row_i in range(len(m)):
        if row_i not in absorbing:
            row_total = float(sum(m[row_i]))
            r_temp = []
            q_temp = []
            for col_i in range(len(m[row_i])):
                if col_i in absorbing:
                    r_temp.append(m[row_i][col_i]/row_total)
                else:
                    q_temp.append(m[row_i][col_i]/row_total)
            r_subm.append(r_temp)
            q_subm.append(q_temp)
    return r_subm, q_subm

def calc_f(q_subm):
    return np.linalg.inv(np.subtract(np.identity(len(q_subm)), q_subm))

def dec_to_frac_with_lcm(l):
    ret_arr = []
    denoms = []
    for num in l:
        frac = Fraction(num).limit_denominator()
        ret_arr.append(frac.numerator)
        denoms.append(frac.denominator)
    lcd = 1
    for denom in denoms:
        lcd = np.lcm(lcd,denom)
    for num_i in range(len(ret_arr)):
        ret_arr[num_i] *= int(lcd/denoms[num_i])
    ret_arr.append(lcd)
    return ret_arr
