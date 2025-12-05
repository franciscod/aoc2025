from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

vals = set()

evs = []
ranges = []
s = 0
ings = False

for l in lines:
    if not ings:
        if not l:
            ings = True
            break
        a, b = l.split('-')
        a = int(a)
        b = int(b)
        s += (b-a+1)
        evs.append((a, 0))
        evs.append((b, 1))

s = 0
depth = 0
beg = 0
for n, e in sorted(evs):
    if e == 0:
        if depth == 0:
            beg = n
        depth += 1

    if e == 1:
        depth -= 1
        if depth == 0:
            k = n - beg + 1
            # print(beg, n, k)
            s += k

print("?")
print(s)
