from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

def maxbank(bank):
    n = 0
    for i, a in enumerate(bank):
        for j, b in enumerate(bank):
            if i >= j:
                continue
            n = max(n, int(a+b))
    return n



s = 0
for r in range(rows):
    bank = ""
    for c in range(cols):
        bank += mp[r,c]
    s += maxbank(bank)

print("?")
print(s)
