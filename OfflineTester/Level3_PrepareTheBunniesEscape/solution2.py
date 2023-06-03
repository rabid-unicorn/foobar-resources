'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.oasys.net/posts/google-foobar-programming-challenge"


#  Mod:
#  Change 'xrange()' to 'range()'


def distance(map):
    # count up distance to each node from start location
    notseen = 999
    d = [
        [1 if i == j == 0 else notseen for j in range(len(row))]
        for i, row in enumerate(map)
    ]

    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x2, y2 = x + move[0], y + move[1]
            if 0 <= x2 < len(d) and 0 <= y2 < len(d[0]):
                if d[x2][y2] == notseen:
                    d[x2][y2] = d[x][y] + 1
                    if not map[x2][y2]:
                        q.append((x2, y2))
    return d


def flip(map):
    # flip a map to have the "end" at (0,0)
    return [[v for v in reversed(row)] for row in reversed(map)]


def solution(map):
    # find the distances starting from both entrance and exit
    b = distance(map)
    e = flip(distance(flip(map)))
    # add the distances and find the shortest point where they intersect
    return min([sum(v) - 1 for i, _ in enumerate(map) for v in zip(b[i], e[i])])
