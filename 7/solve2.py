from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)


def compact(beams):
    r = defaultdict(int)

    for y, x, k, h in beams:
        r[y,x] += k

    s = set()

    for (y, x), k in r.items():
        s.add((y, x, k, ()))

    return s

beams = set()
s = 0
n = 1
for c in rmp['S']:
    beams.add((*c, 1, ()))
    print(c)

for r in range(rows):
    sp = 1
    nbeams = set()
    for y, x, k, h in beams:
        nb = y+1, x
        nh = *h, x
        if mp.get(nb) == '^':
            sp += 1
            nbeams.add((y+1, x-1, k, nh))
            nbeams.add((y+1, x+1, k, nh))
        else:
            nbeams.add((*nb, k, nh))
    beams = compact(nbeams)


print("?")
print(sum([k for y, x, k, _ in beams]))
