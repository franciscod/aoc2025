from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

ps = []
s = 0
for l in lines:
    x, y = parseints(l, ',')
    # print(x, y)
    s += 1
    ps.append((x, y))

area = 0
for a in ps:
    for b in ps:
        if a == b:
            continue
        ax, ay = a
        bx, by = b
        ar = (bx-ax+1)*(by-ay+1)
        if area < ar:
            area = ar


print("?")
print(area)
