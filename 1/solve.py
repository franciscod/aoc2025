from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

s = 0
dial = 50
for l in lines:
    if not l:
        break
    # print(l)
    n = int(l[1:])
    if l[0] == "L":
        n = -n

    dial += n
    dial = (dial + 100) % 100
    if dial == 0:
        s += 1

print("?")
print(s)
