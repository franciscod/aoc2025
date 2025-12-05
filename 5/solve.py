from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)


ranges = []
s = 0
ings = False

def checkfresh(ing):
    for a, b in ranges:
        if a <= ing <= b:
            return True
    return False

for l in lines:
    if not ings:
        if not l:
            ings = True
            continue
        a, b = l.split('-')
        ranges.append((int(a), int(b)))
    else:
        if checkfresh(int(l)):
            s += 1

print("?")
print(s)
