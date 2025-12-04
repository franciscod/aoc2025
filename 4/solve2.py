from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

s = 0
def removable():
    for k in mp:
        if mp[k] != '@':
            continue
        c = 0
        for n in neighs(k, nd8):
            if mp.get(n) == '@':
                c += 1

        if c <4:
            yield k

o = len(mp)
while True:
    ps = list(removable())
    if not ps:
        break
    print(len(ps), ps)
    for p in ps:
        if p in mp:
            del mp[p]

print(o-len(mp))
print("?")
print(s)
