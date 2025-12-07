from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

beams = set()
s = 0
for c in rmp['S']:
    beams.add(c)
    print(c)

for r in range(rows):
    nbeams = set()
    for y, x in beams:
        nb = y+1, x
        if mp.get(nb) == '^':
            s += 1
            nbeams.add((y+1, x-1))
            nbeams.add((y+1, x+1))
        else:
            nbeams.add(nb)
    beams = nbeams
    print(beams)


print("?")
print(s)
