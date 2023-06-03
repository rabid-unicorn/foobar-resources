'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/argcag/foobar2/blob/main/foobar2.py"


#HOW THIS CODE WORKS
#this code works on the fundamental basis that the most efficient way to move towards a place (as a knight) is to move by 2/1, with the 2 in whichever direction the difference is greater.
#eg if the difference is 7 by 5, the default movement should be 2 by 1 (3 by 4 should be 1 by 2, etc). However, there are a certain number of cases where this is not applicable, hence
#cases b-f. An explanation of these cases is attached to the repo page as a jpg file.
#since the movement of cases b-f have not actually been programmed, visualisation of the movement is not possible as it stands, i deemed it unnecessary as it is not in the spec of the q.
#this code IS maintainable to an increased board size, simply increase the rowlength to be greater or smaller than 8. note: calculation may not be accurate for smaller boards, as some
#movement requires moving around outside of the board to find the most efficient path.


def solution(src,dest):
    rowlength = 8
    sy = src // rowlength #starting y coord (which array from the 2d array/which row)
    sx = src % rowlength #starting x coord (index of pos per array/which column)
    ey = dest // rowlength #end y coord
    ex = dest % rowlength #end x coord
    dy = sy-ey # difference in y
    dx = sx-ex # difference in x
    moves = 0 #total (counting) number of moves required to reach end from start


    while dy != 0 or dx != 0:
        if dy<0: dy *= -1 #it doesnt actually matter which direction it is moving in,
        if dx<0: dx *= -1 #since the movement will be mirrored either way.

        ###MOVEMENT
        if (dy == 0 and dx == 1) or (dy == 1 and dx == 0): #b
            moves += 3
            break
        
        elif (dy == 1 and dx == 1): #c
            if sy == 0 or sy == 7:      #extra care has to be taken with c, because if the start or end is at a corner, the default movement symbolised by c cannot be performed,
                if sx == 0 or sx == 7:  # (it would have to jump off the board to do so) so a compromise movement (which is actually a,b or -a,d respectively) would be used (4m)
                    moves += 4
            elif ey == 0 or ey == 7:
                if ex == 0 or ex == 7:
                    moves += 4
            else:
                moves += 2
            break
        
        elif (dy == 3 and dx == 1) or (dy == 1 and dx == 3): #d
            moves += 2
            break
        
        elif (dy == 2 and dx == 0) or (dy == 0 and dx == 2): #e
            moves += 2
            break
        
        elif (dy == 4 and dx == 3) or (dy == 3 and dx == 4): #f
            moves += 3
            break
        
        else: #a
            if dy>dx:
                dy -= 2 ; dx -= 1
            elif dx>dy:
                dy -= 1 ; dx -= 2
            else:
                dy -= 2 ; dx -= 1 #if distance is 1,1 for example, it doesnt matter
                                  #which way it goes i just put vertical preference.
            moves += 1
            
        
    return moves
