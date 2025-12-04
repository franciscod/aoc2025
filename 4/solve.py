from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

s = 0
for k in mp:
    print(mp[k])
    c = 0
    for n in neighs(k, nd8):
        if mp.get(n) == '@':
            c += 1

    if c <4:
        s += 1

print("?")
print(s)
